import numpy as np
from sklearn.linear_model import LinearRegression

rng = np.random.default_rng(0)
n, d = 500, 3
X = rng.normal(size=(n, d))
true_w = np.array([2.0, -1.5, 0.5])
true_b = 4.0
y = X @ true_w + true_b + rng.normal(0, 0.5, n)

Xb = np.hstack([np.ones((n, 1)), X])      # intercept column

# 1. normal equation, solved not inverted
w_closed = np.linalg.solve(Xb.T @ Xb, Xb.T @ y)

# 2. gradient descent
w = np.zeros(d + 1)
eta = 0.05
for step in range(2000):
    grad = -(2 / n) * Xb.T @ (y - Xb @ w)
    w -= eta * grad

# 3. the library
sk = LinearRegression().fit(X, y)

print('truth       :', np.r_[true_b, true_w].round(3))
print('closed form :', w_closed.round(3))
print('gradient    :', w.round(3))
print('sklearn     :', np.r_[sk.intercept_, sk.coef_].round(3))
