import pandas as pd

def revenue_by_country_category(df):
    """Country × Category table of total revenue, zeros where empty."""
    frame = df.assign(Revenue=df["Quantity"] * df["UnitPrice"])
    table = frame.pivot_table(values="Revenue", index="Country", columns="Category",
                              aggfunc="sum", fill_value=0)
    return table.sort_index().sort_index(axis=1)
