import numpy as np, warnings; warnings.filterwarnings("ignore")

def make_problem(cond=1.0, n=800, d=2, seed=0):
    """A least-squares problem whose curvature ratio we control."""
    rng = np.random.default_rng(seed)
    X = rng.normal(size=(n, d))
    X[:, 1] *= cond                       # stretch one axis
    w_true = np.array([2.0, -1.0])
    y = X @ w_true + rng.normal(0, 0.3, n)
    return X, y, w_true

def loss(X, y, w):
    r = X @ w - y
    return float(r @ r / len(y))

def grad(X, y, w):
    return 2 * X.T @ (X @ w - y) / len(y)
