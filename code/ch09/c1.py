import numpy as np, pandas as pd
df = pd.read_csv("retail.csv")
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
clean = df[~df["InvoiceNo"].str.startswith("C")].copy()
o = clean.groupby("InvoiceNo").agg(
    rev=("Revenue", "sum"), units=("Quantity", "sum"),
    lines=("Revenue", "size"))

w = np.array([12.0, 25.0])     # value per unit, per extra line
b = 20.0                       # base

# one order, by hand and by dot product
x = np.array([o["units"].iloc[0], o["lines"].iloc[0]])
print("features:", x)
print("by hand: ", x[0]*w[0] + x[1]*w[1] + b)
print("dot:     ", x @ w + b)

# every order, in one operation
X = o[["units", "lines"]].values.astype(float)
preds = X @ w + b
print(f"\nX {X.shape} @ w {w.shape} -> preds {preds.shape}")
print("first five:", np.round(preds[:5], 2))
