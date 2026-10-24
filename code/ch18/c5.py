# Schedules earn their place when the gradient is noisy. With mini-batches
# a constant rate plateaus at a noise floor it cannot get below.
X, y, _ = make_problem(cond=10, n=8000)
best = loss(X, y, np.linalg.lstsq(X, y, rcond=None)[0])
ETA0, BATCH, EPOCHS = 0.006, 64, 12

def run(sched):
    rng = np.random.default_rng(0)
    w = np.zeros(2)
    per_epoch = len(y) // BATCH
    total = per_epoch * EPOCHS
    t = 0
    for _ in range(EPOCHS):
        idx = rng.permutation(len(y))
        for b in range(per_epoch):
            t += 1
            if sched == "constant":
                eta = ETA0
            elif sched == "step":
                eta = ETA0 * (0.1 ** (t // (total // 3)))
            else:                                # cosine decay to zero
                eta = ETA0 * 0.5 * (1 + np.cos(np.pi * t / total))
            sl = idx[b * BATCH:(b + 1) * BATCH]
            w -= eta * grad(X[sl], y[sl], w)
    return loss(X, y, w)

for s in ("constant", "step", "cosine"):
    l = run(s)
    print(f"{s:<10} final loss {l:.6f}   excess over best {l - best:.2e}")
print(f"\nbest achievable on this data: {best:.6f}")
