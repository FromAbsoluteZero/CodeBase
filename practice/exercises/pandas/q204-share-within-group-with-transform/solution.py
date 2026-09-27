import pandas as pd

def line_share(df):
    """Each line's share of its invoice's revenue, aligned to df.index."""
    revenue = df["Quantity"] * df["UnitPrice"]
    invoice_total = revenue.groupby(df["InvoiceNo"]).transform("sum")
    return revenue / invoice_total
