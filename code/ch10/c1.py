import numpy as np, pandas as pd
df = pd.read_csv("retail.csv")
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
clean = df[~df["InvoiceNo"].str.startswith("C")].copy()
o = clean.groupby("InvoiceNo").agg(
    rev=("Revenue", "sum"), units=("Quantity", "sum"))

x = o["units"].values.astype(float)
y = o["rev"].values.astype(float)
xz = (x - x.mean()) / x.std()          # standardize, per Chapter 9

b0, b1, eta = 0.0, 0.0, 0.1
for step in range(200):
    pred = b0 + b1 * xz
    err = pred - y
    g0 = 2 * err.mean()                # slope for the intercept
    g1 = 2 * (err * xz).mean()         # slope for the coefficient
    b0 -= eta * g0                     # step against the gradient
    b1 -= eta * g1
    if step in (0, 5, 20, 199):
        print(f"step {step:>3}: loss {(err**2).mean():>10,.0f}")

slope = b1 / x.std()
intercept = b0 - b1 * x.mean() / x.std()
print(f"\ngradient descent: intercept {intercept:.4f} "
      f"slope {slope:.4f}")

beta = np.linalg.lstsq(np.column_stack([np.ones(len(x)), x]),
                       y, rcond=None)[0]
print(f"exact algebra:    intercept {beta[0]:.4f} "
      f"slope {beta[1]:.4f}")
