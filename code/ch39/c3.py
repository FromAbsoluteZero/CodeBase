# LoRA: freeze the pretrained matrix entirely and train only a low-rank
# update A @ B added on top of it. The rank r controls exactly how many
# parameters this costs: D*r for A, plus r*D for B.
def train_lora(Xtr, Htr_target, Xte, Hte_target, W_frozen, rank, seed, epochs=300, eta=1.0):
    rr = np.random.default_rng(seed)
    A = rr.normal(0, 0.01, (D, rank))          # small init, as the LoRA paper prescribes
    B = np.zeros((rank, D))                     # B starts at zero: the update starts at zero
    for _ in range(epochs):
        W = W_frozen + A @ B
        H = np.tanh(Xtr @ W)
        dH = 2 * (H - Htr_target) * (1 - H**2) / len(Xtr)
        dW = Xtr.T @ dH                          # gradient w.r.t. the full update
        dA = dW @ B.T
        dB = A.T @ dW
        A -= eta * dA; B -= eta * dB
    W_final = W_frozen + A @ B
    return A, B, mse_loss(W_final, Xte, Hte_target)

print(f"{'rank':>6}{'trainable params':>18}{'% of full':>12}{'held-out MSE':>14}")
for rank in (1, 2, 4, 8, 16, 32):
    n_params = D * rank * 2
    _, _, loss = train_lora(Xtr, Htr_target, Xte, Hte_target, W_pretrained,
                            rank=rank, seed=39)
    print(f"{rank:>6}{n_params:>18,}{100*n_params/full_params:>12.2f}{loss:>14.6f}")

print(f"\nfor reference: unadapted {loss_frozen:.4f}, full fine-tune {loss_full:.6f} "
      f"({full_params:,} params)")
