# The learning rate is the one setting that decides whether training
# works at all. Chapter 10 showed this on one problem; here is the rule.
X, y, w_true = make_problem()
L = 2 * np.linalg.eigvalsh(X.T @ X / len(y)).max()    # curvature bound
print(f"largest curvature of this loss: {L:.3f}")
print(f"gradient descent diverges above eta = 2/L = {2/L:.4f}\n")

print(f"{'eta':>8}{'loss after 200 steps':>24}{'verdict':>14}")
for eta in (0.001, 0.01, 0.1, 0.5, 0.9, 1.05):
    w = np.zeros(2)
    for _ in range(200):
        w -= eta * grad(X, y, w)
        if not np.isfinite(w).all():
            break
    l = loss(X, y, w)
    verdict = ("diverged" if not np.isfinite(l) or l > 1e3
               else "crawling" if l > 0.2 else "converged")
    shown = "overflow" if not np.isfinite(l) else f"{l:.4f}"
    print(f"{eta:>8.3f}{shown:>24}{verdict:>14}")
