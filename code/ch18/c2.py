# Why plain descent is slow: it is not the learning rate, it is the shape.
print(f"{'stretch':>9}{'condition':>12}{'steps to loss<0.11':>21}{'best eta':>10}")
for c in (1, 3, 10, 30):
    X, y, _ = make_problem(cond=c)
    H = 2 * X.T @ X / len(y)
    ev = np.linalg.eigvalsh(H)
    best, best_steps = None, None
    for eta in np.geomspace(1e-4, 2 / ev.max() * 0.99, 60):
        w, steps = np.zeros(2), None
        for i in range(1, 4001):
            w -= eta * grad(X, y, w)
            if not np.isfinite(w).all():
                break
            if loss(X, y, w) < 0.11:
                steps = i
                break
        if steps and (best_steps is None or steps < best_steps):
            best, best_steps = eta, steps
    print(f"{c:>9}{ev.max()/ev.min():>12.1f}{best_steps:>21}{best:>10.4f}")
