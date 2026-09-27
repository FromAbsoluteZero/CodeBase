# Full-batch descent uses every row per step. Mini-batches use a sample,
# so each step is noisier and vastly cheaper.
rng = np.random.default_rng(0)
X, y, _ = make_problem(cond=10, n=8000)

def sgd(batch, eta, epochs=8):
    w = np.zeros(2)
    n = len(y)
    per_epoch = max(n // batch, 1)
    hist = []
    for _ in range(epochs):
        idx = rng.permutation(n)
        for b in range(per_epoch):
            sl = idx[b * batch:(b + 1) * batch]
            w -= eta * grad(X[sl], y[sl], w)
        hist.append(loss(X, y, w))
    return hist, per_epoch * epochs

print(f"{'batch size':>11}{'updates':>9}{'rows seen':>11}{'final loss':>12}")
for batch in (8000, 512, 64, 8):
    h, upd = sgd(batch, 0.0094 if batch == 8000 else 0.005)
    print(f"{batch:>11}{upd:>9}{upd*batch:>11,}{h[-1]:>12.4f}")
