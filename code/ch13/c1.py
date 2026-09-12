import pandas as pd, numpy as np
from scipy import stats

df = pd.read_csv("retail.csv").drop_duplicates()
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
clean = df[~df["InvoiceNo"].str.startswith("C")].copy()
o = clean.groupby("InvoiceNo").agg(
    rev=("Revenue", "sum"), units=("Quantity", "sum"),
    lines=("Revenue", "size"), country=("Country", "first"))

r = stats.linregress(o["units"], o["rev"])
print(f"slope       {r.slope:8.4f}  per unit")
print(f"intercept   {r.intercept:8.4f}")
print(f"std error   {r.stderr:8.4f}")
print(f"r           {r.rvalue:8.4f}")
print(f"R-squared   {r.rvalue**2:8.4f}")
print(f"p-value     {r.pvalue:8.3e}")
print(f"95% CI on the slope: "
      f"[{r.slope - 1.96*r.stderr:.2f}, "
      f"{r.slope + 1.96*r.stderr:.2f}]")
