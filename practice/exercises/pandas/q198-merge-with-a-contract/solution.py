import pandas as pd

def invoice_totals(df):
    """One row per InvoiceNo with its InvoiceTotal."""
    revenue = df["Quantity"] * df["UnitPrice"]
    return (revenue.groupby(df["InvoiceNo"]).sum()
            .rename("InvoiceTotal").reset_index())

def add_invoice_total(df, totals=None):
    """The lines of df with InvoiceTotal attached (left merge, validate='m:1').
    `totals` defaults to invoice_totals(df); the check passes a bad one to see the merge refuse it."""
    if totals is None:
        totals = invoice_totals(df)
    return df.merge(totals, on="InvoiceNo", how="left", validate="m:1")
