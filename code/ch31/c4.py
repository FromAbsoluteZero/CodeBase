# Train a genuinely deep network two ways: naive initialization against
# He initialization. Same architecture, same data, same learning rate.
def forward_deep(x, Ws, bs):
    acts = [x]
    for i, (W, b) in enumerate(zip(Ws, bs)):
        z = acts[-1] @ W + b
        a = softmax(z) if i == len(Ws) - 1 else np.maximum(0, z)
        acts.append(a)
    return acts

def train(sizes, init_fn, seed, eta, epochs=250):
    Ws = init_fn(sizes, seed=seed)
    bs = [np.zeros(s) for s in sizes[1:]]
    Ytr = np.eye(10)[ytr]
    history = []
    for epoch in range(epochs + 1):
        acts = forward_deep(Xtr, Ws, bs)
        p = acts[-1]
        loss = -np.sum(Ytr * np.log(p + 1e-12)) / len(Xtr)
        d = (p - Ytr) / len(Xtr)
        grads_W, grads_b = [], []
        for i in reversed(range(len(Ws))):
            gW = acts[i].T @ d
            gb = d.sum(0)
            grads_W.insert(0, gW); grads_b.insert(0, gb)
            if i > 0:
                d = (d @ Ws[i].T) * (acts[i] > 0)
        for i in range(len(Ws)):
            Ws[i] -= eta * grads_W[i]; bs[i] -= eta * grads_b[i]
        if epoch % 50 == 0:
            test_acts = forward_deep(Xte, Ws, bs)
            acc = (test_acts[-1].argmax(1) == yte).mean()
            history.append((epoch, loss, acc))
    return history

print("naive initialization")
for ep, loss, acc in train(deep_sizes, naive_init, seed=31, eta=0.05):
    print(f"  epoch {ep:>4}  loss {loss:>10.4f}  test acc {acc:.4f}")

print("\nHe initialization, same architecture, same learning rate")
for ep, loss, acc in train(deep_sizes, he_init, seed=31, eta=0.05):
    print(f"  epoch {ep:>4}  loss {loss:>10.4f}  test acc {acc:.4f}")
