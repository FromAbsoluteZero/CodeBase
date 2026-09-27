D = pd.get_dummies(o["country"], prefix="", prefix_sep="",
                   drop_first=True).astype(float)
Xc = np.column_stack([np.ones(len(o)), o["units"], D.values])
nm = ["intercept", "units"] + list(D.columns)
bc = np.linalg.lstsq(Xc, y, rcond=None)[0]
ec = y - Xc @ bc
sec = np.sqrt(np.diag((ec**2).sum()/(len(y)-Xc.shape[1])
                      * np.linalg.inv(Xc.T@Xc)))
pc = 2*(1 - stats.t.cdf(np.abs(bc/sec), len(y)-Xc.shape[1]))
for n_, b_, p_ in zip(nm, bc, pc):
    print(f"  {n_:<16}{b_:>8.2f}   p={p_:.4f}")
print(f"R-squared {1 - (ec**2).sum()/((y-y.mean())**2).sum():.4f}")
