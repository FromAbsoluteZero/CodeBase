D = pd.get_dummies(o["country"], prefix="c",
                   drop_first=True).astype(float)
print("reference category:", sorted(o['country'].unique())[0])
print("dummy columns:", list(D.columns))

X2 = np.column_stack([np.ones(len(o)), o["units"], o["lines"], D.values])
names2 = ["intercept", "units", "lines"] + list(D.columns)

b2 = np.linalg.lstsq(X2, y, rcond=None)[0]
r2_ = y - X2 @ b2
n2, k2 = X2.shape
se2 = np.sqrt(np.diag((r2_**2).sum()/(n2-k2) * np.linalg.inv(X2.T @ X2)))
p2 = 2 * (1 - stats.t.cdf(np.abs(b2/se2), n2-k2))

for nm, b_, p_ in zip(names2, b2, p2):
    star = "  *" if p_ < 0.05 else ""
    print(f"  {nm:<18}{b_:>9.2f}   p={p_:.4f}{star}")
print(f"\nR-squared {1 - (r2_**2).sum()/((y-y.mean())**2).sum():.4f}")
