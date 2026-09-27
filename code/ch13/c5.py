def vif(X, j):
    """Regress column j on the others; return 1 / (1 - R2)."""
    others = np.delete(X, j, axis=1)
    target = X[:, j]
    b = np.linalg.lstsq(others, target, rcond=None)[0]
    r2 = 1 - ((target - others @ b)**2).sum() / \
             ((target - target.mean())**2).sum()
    return 1 / (1 - r2)

print(f"corr(units, lines) = "
      f"{np.corrcoef(o['units'], o['lines'])[0,1]:.4f}")
print(f"VIF units = {vif(X, 1):.3f}")
print(f"VIF lines = {vif(X, 2):.3f}")

# what dropping the redundant predictor costs
Xs = np.column_stack([np.ones(len(o)), o["units"]])
bs = np.linalg.lstsq(Xs, y, rcond=None)[0]
rs = y - Xs @ bs
print(f"\nR-squared with lines:    {r2:.4f}")
print(f"R-squared without lines: "
      f"{1 - (rs**2).sum()/((y-y.mean())**2).sum():.4f}")
