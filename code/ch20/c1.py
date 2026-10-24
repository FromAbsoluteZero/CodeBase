# Why averaging helps at all, before any trees are involved. Each "model"
# is an unbiased but noisy estimate of the same truth. What matters is not
# how many you average but how much their errors have in common.
print(f"{'corr':>6}{'k=1':>9}{'k=10':>9}{'k=100':>9}{'reduction':>12}")
for corr in (0.0, 0.3, 0.6, 0.9):
    shared = rng.normal(0, np.sqrt(corr), 8000)
    own = rng.normal(0, np.sqrt(1 - corr), (8000, 100))
    row = []
    for k in (1, 10, 100):
        row.append((shared[:, None] + own[:, :k]).mean(1).var())
    print(f"{corr:>6.1f}{row[0]:>9.3f}{row[1]:>9.3f}{row[2]:>9.3f}"
          f"{row[0] / row[2]:>11.1f}x")
