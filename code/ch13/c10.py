fit = Xc @ bc
print(f"residual mean:  {ec.mean():.6f}")
print(f"residual skew:  {pd.Series(ec).skew():.3f}")
print(f"corr(|resid|, fitted): {np.corrcoef(np.abs(ec), fit)[0,1]:.4f}")

band = pd.qcut(fit, 3, labels=["small", "medium", "large"])
print("\ntypical error by predicted size:")
print(pd.Series(ec).groupby(band, observed=True).std().round(0).to_string())
