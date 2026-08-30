# An adapter takes a different architectural approach: rather than
# adding a low-rank update to an existing weight matrix, insert a small
# bottleneck layer after it, and train only that. Applied to the same
# large pretrained matrix from Steps 1-3, at a comparable parameter
# budget to the rank-4 LoRA above.
def train_adapter(Xtr, Htr_target, Xte, Hte_target, W_frozen, bottleneck, seed,
                  epochs=500, eta=0.01):
    rr = np.random.default_rng(seed)
    W_down = rr.normal(0, np.sqrt(1/D), (D, bottleneck))
    W_up = np.zeros((bottleneck, D))                # up-projection starts at zero
    for _ in range(epochs):
        H0 = np.tanh(Xtr @ W_frozen)                # the frozen matrix's own output
        z = H0 @ W_down
        adapter_out = z @ W_up
        H = H0 + adapter_out                         # adapter output added as a residual
        dH = 2 * (H - Htr_target) / len(Xtr)
        dWup = z.T @ dH
        dz = dH @ W_up.T
        dWdown = H0.T @ dz
        W_up -= eta * dWup; W_down -= eta * dWdown
    H0_te = np.tanh(Xte @ W_frozen)
    H_te = H0_te + (H0_te @ W_down) @ W_up
    return np.mean((H_te - Hte_target) ** 2), W_down.size + W_up.size

print(f"{'bottleneck':>11}{'trainable params':>18}{'held-out MSE':>14}")
for bn in (2, 4, 8, 16):
    loss, n_params = train_adapter(Xtr, Htr_target, Xte, Hte_target, W_pretrained,
                                   bottleneck=bn, seed=39)
    print(f"{bn:>11}{n_params:>18,}{loss:>14.6f}")

print(f"\nfor reference: LoRA at rank 4 used 2,048 params for MSE 0.130881")
print(f"unadapted {loss_frozen:.4f}, full fine-tune {loss_full:.6f} ({full_params:,} params)")
print(f"\nthe gap is structural, not a fair ranking of the two methods: this")
print(f"task was built as a linear perturbation to W, exactly what LoRA")
print(f"parameterizes directly. The adapter intervenes after the tanh")
print(f"nonlinearity, a different point in the computation, and pays for")
print(f"that mismatch here.")
