import pandas as pd
df = pd.read_csv("retail.csv")
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
clean = df[~df["InvoiceNo"].str.startswith("C")].copy()

orders = clean.groupby("InvoiceNo").agg(
    rev=("Revenue", "sum"), country=("Country", "first"))
orders["big"] = orders["rev"] > 300

p_big = orders["big"].mean()
print(f"P(order > $300)      = {p_big:.4f}")
print(f"P(order <= $300)     = {1 - p_big:.4f}  (complement)")
print(f"they sum to          = {p_big + (1 - p_big):.4f}")
print(f"count of big orders  = {orders['big'].sum()} of {len(orders)}")
