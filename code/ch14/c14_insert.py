import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=800, n_features=4,
                           n_informative=3, n_redundant=0,
                           n_clusters_per_class=1, class_sep=0.9,
                           random_state=0)
Xb = np.hstack([np.ones((len(X), 1)), X])       # intercept column

def sigmoid(z):
    # clip keeps exp() from overflowing on large negative z
    return 1.0 / (1.0 + np.exp(-np.clip(z, -500, 500)))

w = np.zeros(Xb.shape[1])
eta = 0.5
for step in range(20000):
    p = sigmoid(Xb @ w)
    grad = Xb.T @ (p - y) / len(y)       # same form as Chapter 13's
    w -= eta * grad
    if step % 5000 == 0:
        loss = -np.mean(y * np.log(p + 1e-12) +
                        (1 - y) * np.log(1 - p + 1e-12))
        print(f"step {step:>6}  log loss {loss:.4f}")

sk = LogisticRegression(C=1e6, max_iter=10000).fit(X, y)
print("mine   :", w.round(2))
print("sklearn:", np.r_[sk.intercept_, sk.coef_[0]].round(2))
