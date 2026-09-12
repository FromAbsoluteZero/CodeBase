import numpy as np
rng = np.random.default_rng(0)

# Where squared error comes from: assume the noise is Gaussian, then ask
# which parameters make the observed data most likely.
true_mu, true_sd, n = 4.0, 0.5, 400
data = rng.normal(true_mu, true_sd, n)

def neg_log_lik(mu):
    # log of the Gaussian density, summed, negated. Constants dropped.
    return np.sum((data - mu) ** 2) / (2 * true_sd ** 2)

grid = np.linspace(3.0, 5.0, 20001)
mle = grid[np.argmin([neg_log_lik(m) for m in grid])]

print(f"maximum likelihood estimate: {mle:.4f}")
print(f"sample mean:                 {data.mean():.4f}")
print(f"they are the same estimator: {abs(mle - data.mean()) < 1e-3}")

# The same logic with a yes-or-no outcome gives cross-entropy instead.
y = (rng.random(n) < 0.3).astype(int)
def neg_log_lik_bernoulli(p):
    return -np.sum(y * np.log(p) + (1 - y) * np.log(1 - p)) / n

ps = np.linspace(0.01, 0.99, 9801)
mle_p = ps[np.argmin([neg_log_lik_bernoulli(p) for p in ps])]
print(f"\nBernoulli MLE: {mle_p:.4f}   sample proportion: {y.mean():.4f}")
print(f"loss at the MLE: {neg_log_lik_bernoulli(mle_p):.4f}"
      f"   (this quantity is log loss)")
