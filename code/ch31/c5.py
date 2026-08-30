# Batch normalization rescales each layer's output to zero mean, unit
# variance, using the statistics of the current batch, then lets the
# network learn a scale and shift back if it wants one.
def forward_bn(x, Ws, bs, gammas, betas, eps=1e-5):
    acts = [x]
    for i, (W, b) in enumerate(zip(Ws, bs)):
        z = acts[-1] @ W + b
        if i < len(Ws) - 1:
            mu, var = z.mean(0), z.var(0)
            z_norm = (z - mu) / np.sqrt(var + eps)
            z = gammas[i] * z_norm + betas[i]
            a = np.maximum(0, z)
        else:
            a = softmax(z)
        acts.append(a)
    return acts

def train_bn(sizes, init_fn, seed, eta, epochs=250):
    Ws = init_fn(sizes, seed=seed)
    bs = [np.zeros(s) for s in sizes[1:]]
    gammas = [np.ones(s) for s in sizes[1:-1]]
    betas = [np.zeros(s) for s in sizes[1:-1]]
    Ytr = np.eye(10)[ytr]
    history = []
    for epoch in range(epochs + 1):
        acts = forward_bn(Xtr, Ws, bs, gammas, betas)
        p = acts[-1]
        loss = -np.sum(Ytr * np.log(p + 1e-12)) / len(Xtr)
        d = (p - Ytr) / len(Xtr)
        for i in reversed(range(len(Ws))):
            gW = acts[i].T @ d
            gb = d.sum(0)
            Ws[i] -= eta * gW; bs[i] -= eta * gb
            if i > 0:
                d = (d @ Ws[i].T) * (acts[i] > 0)
        if epoch % 50 == 0:
            test_acts = forward_bn(Xte, Ws, bs, gammas, betas)
            acc = (test_acts[-1].argmax(1) == yte).mean()
            history.append((epoch, loss, acc))
    return history

print("naive initialization, WITH batch normalization")
for ep, loss, acc in train_bn(deep_sizes, naive_init, seed=31, eta=0.05):
    print(f"  epoch {ep:>4}  loss {loss:>10.4f}  test acc {acc:.4f}")
