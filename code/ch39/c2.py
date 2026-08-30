# A regression framing: the loss is direct mean-squared error between
# the current matrix's hidden representation and the target
# transformation's hidden representation, on unlabelled input vectors.
# This is closer to how LoRA is actually posed, and it removes the
# classification-boundary noise that would otherwise obscure what the
# rank itself is doing.
def make_inputs(n, seed):
    return np.random.default_rng(seed).normal(size=(n, D))

Xtr = make_inputs(2000, seed=101)
Xte = make_inputs(500, seed=102)
Htr_target = np.tanh(Xtr @ W_target_true)          # what the target task actually wants
Hte_target = np.tanh(Xte @ W_target_true)

def mse_loss(W, X, H_target):
    H = np.tanh(X @ W)
    return np.mean((H - H_target) ** 2)

def train_full(Xtr, Htr_target, Xte, Hte_target, W_init, epochs=300, eta=1.0):
    W = W_init.copy()
    for _ in range(epochs):
        H = np.tanh(Xtr @ W)
        dH = 2 * (H - Htr_target) * (1 - H**2) / len(Xtr)
        dW = Xtr.T @ dH
        W -= eta * dW
    return W, mse_loss(W, Xte, Hte_target)

loss_frozen = mse_loss(W_pretrained, Xte, Hte_target)
W_full, loss_full = train_full(Xtr, Htr_target, Xte, Hte_target, W_pretrained)

print(f"held-out MSE, unadapted pretrained matrix: {loss_frozen:.4f}")
print(f"held-out MSE, after FULL fine-tuning ({full_params:,} params): {loss_full:.6f}")
print(f"\n(a perfect match to the target transformation gives MSE 0)")
