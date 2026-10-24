import pandas as pd

def rfm(df, as_of="2024-12-31"):
    """RFM table indexed by CustomerID with Recency, Frequency, Monetary, R, F, M."""
    known = df[df["CustomerID"].notna()].copy()
    known["Revenue"] = known["Quantity"] * known["UnitPrice"]
    known["InvoiceDate"] = pd.to_datetime(known["InvoiceDate"])
    per_customer = known.groupby("CustomerID").agg(
        LastDate=("InvoiceDate", "max"),
        Frequency=("InvoiceNo", "nunique"),
        Monetary=("Revenue", "sum"),
    )
    table = pd.DataFrame({
        "Recency": (pd.Timestamp(as_of) - per_customer["LastDate"]).dt.days,
        "Frequency": per_customer["Frequency"],
        "Monetary": per_customer["Monetary"],
    })
    def score(series, labels):
        return pd.qcut(series.rank(method="first"), 4, labels=labels).astype(int)
    table["R"] = score(table["Recency"], [4, 3, 2, 1])
    table["F"] = score(table["Frequency"], [1, 2, 3, 4])
    table["M"] = score(table["Monetary"], [1, 2, 3, 4])
    return table

def top_segment_count(rfm_table):
    """Number of customers whose R + F + M is at least 10."""
    total = rfm_table["R"] + rfm_table["F"] + rfm_table["M"]
    return int((total >= 10).sum())
