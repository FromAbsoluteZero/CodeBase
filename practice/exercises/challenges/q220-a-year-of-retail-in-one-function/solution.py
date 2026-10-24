import pandas as pd

def retail_summary(df):
    """The seven figures described in README.md, as a dictionary."""
    revenue = df["Quantity"] * df["UnitPrice"]
    cancelled = df["InvoiceNo"].astype(str).str.startswith("C")
    gross = revenue[~cancelled].sum()
    monthly = revenue.groupby(df["InvoiceDate"].str[:7]).sum()
    by_category = revenue.groupby(df["Category"]).sum()
    known = df[df["CustomerID"].notna()]
    invoices_per_customer = known.groupby("CustomerID")["InvoiceNo"].nunique()
    return {
        "net_revenue": float(revenue.sum()),
        "cancellation_share": float(-revenue[cancelled].sum() / gross),
        "best_month": monthly.idxmax(),
        "worst_month": monthly.idxmin(),
        "top_category": by_category.idxmax(),
        "top_category_share": float(by_category.max() / revenue.sum()),
        "repeat_customer_share": float((invoices_per_customer > 1).mean()),
    }
