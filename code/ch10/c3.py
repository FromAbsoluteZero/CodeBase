import numpy as np

def loss(w):                        # a small stand-in for a real loss
    return np.sum(w ** 2) + 3 * w[0]

def analytic_grad(w):
    g = 2 * w
    g[0] += 3
    return g

def numeric_grad(f, w, h=1e-5):
    """Central difference: perturb each parameter both ways."""
    g = np.zeros_like(w)
    for i in range(len(w)):
        up, down = w.copy(), w.copy()
        up[i] += h
        down[i] -= h
        g[i] = (f(up) - f(down)) / (2 * h)
    return g

w = np.array([1.5, -2.0, 0.7])
a, n = analytic_grad(w.copy()), numeric_grad(loss, w)
print("analytic:", a.round(6))
print("numeric :", n.round(6))
print("agree   :", np.allclose(a, n, atol=1e-7))

# A zero gradient is a stationary point, not necessarily a minimum.
saddle = lambda p: p[0] ** 2 - p[1] ** 2
at = np.array([0.0, 0.0])
print(f"\nsaddle gradient at origin: {numeric_grad(saddle, at).round(9)}")
print(f"  step along x: {saddle(np.array([0.01, 0.0])):+.5f}  (loss rises)")
print(f"  step along y: {saddle(np.array([0.0, 0.01])):+.5f}  (loss falls)")
