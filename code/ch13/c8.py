y = o["rev"].values
X = np.column_stack([np.ones(len(o)), o["units"], o["lines"]])
b = np.linalg.lstsq(X, y, rcond=None)[0]
e = y - X @ b
se = np.sqrt(np.diag((e**2).sum()/(len(y)-3) * np.linalg.inv(X.T@X)))
p = 2 * (1 - stats.t.cdf(np.abs(b/se), len(y)-3))

print(f"lines coefficient: {b[2]:.3f} (se {se[2]:.3f}, p {p[2]:.3f})")
print(f"R-squared {1 - (e**2).sum()/((y-y.mean())**2).sum():.4f} "
      f"(was {r.rvalue**2:.4f})")
print(f"VIF for lines: {vif(X, 2):.2f} — it overlaps with units")
