import pandas as pd

def gross_and_net(df):
    """Per-category Gross (no cancellations) and Net (all lines) revenue."""
    revenue = df["Quantity"] * df["UnitPrice"]
    cancelled = df["InvoiceNo"].astype(str).str.startswith("C")
    gross = revenue[~cancelled].groupby(df["Category"][~cancelled]).sum()
    net = revenue.groupby(df["Category"]).sum()
    return pd.DataFrame({"Gross": gross, "Net": net}).sort_index()
