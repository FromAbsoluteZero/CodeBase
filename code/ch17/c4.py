import pandas as pd
df = pd.read_csv("retail.csv")
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
clean = df[~df["InvoiceNo"].str.startswith("C")].copy()

o = clean.groupby("InvoiceNo").agg(
        rev=("Revenue", "sum"), units=("Quantity", "sum"),
        lines=("StockCode", "count"),
        avg_price=("UnitPrice", "mean")).reset_index()

# Two features that genuinely matter, one near-duplicate of units,
# and six columns of pure noise -- the shape of a real feature table.
o["units_copy"] = o["units"] * 1.02 + rng.normal(0, .3, len(o))
for j in range(6):
    o[f"noise_{j}"] = rng.normal(0, 1, len(o))

feats = ["units", "lines", "avg_price", "units_copy"] + \
        [f"noise_{j}" for j in range(6)]
print(f"{len(o):,} orders, {len(feats)} candidate features")
print(f"correlation units vs units_copy: "
      f"{o['units'].corr(o['units_copy']):.3f}")
