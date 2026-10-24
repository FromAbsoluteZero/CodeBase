import numpy as np
rng = np.random.default_rng(0)

def truth(x):                       # the relationship, unknown to any model
    return np.sin(1.4 * x) + 0.3 * x

def sample(n=40):
    x = rng.uniform(-3, 3, n)
    return x, truth(x) + rng.normal(0, 0.45, n)

xs = np.linspace(-3, 3, 200)        # where we measure
runs = 300                          # 300 alternative worlds
NOISE = 0.45 ** 2

print(f"{'degree':>7}{'bias^2':>9}{'variance':>10}{'noise':>8}{'total':>10}")
for deg in [1, 2, 3, 5, 7, 9, 12]:
    preds = np.zeros((runs, len(xs)))
    for r in range(runs):
        x, y = sample()
        preds[r] = np.polyval(np.polyfit(x, y, deg), xs)
    bias2 = ((preds.mean(0) - truth(xs)) ** 2).mean()
    var = preds.var(0).mean()
    print(f"{deg:>7}{bias2:>9.3f}{var:>10.3f}{NOISE:>8.3f}"
          f"{bias2 + var + NOISE:>10.3f}")
