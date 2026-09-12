y = o["rev"].values
X = np.column_stack([np.ones(len(o)), o["units"], o["lines"]])
names = ["intercept", "units", "lines"]

beta = np.linalg.lstsq(X, y, rcond=None)[0]
resid = y - X @ beta
n, k = X.shape
s2 = (resid**2).sum() / (n - k)
se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
t = beta / se
p = 2 * (1 - stats.t.cdf(np.abs(t), n - k))

print(f"{'':<10}{'coef':>10}{'std err':>10}{'t':>8}{'p':>10}")
for nm, b_, s_, t_, p_ in zip(names, beta, se, t, p):
    print(f"{nm:<10}{b_:>10.3f}{s_:>10.3f}{t_:>8.2f}{p_:>10.3f}")

r2 = 1 - (resid**2).sum() / ((y - y.mean())**2).sum()
adj = 1 - (1 - r2) * (n - 1) / (n - k)
print(f"\nR-squared {r2:.4f}   adjusted {adj:.4f}")
print(f"residual sd ${np.sqrt(s2):,.2f}")
