import pandas as pd

def is_unique_grain(df, keys):
    """True if the columns in `keys` identify every row uniquely."""
    return not bool(df.duplicated(subset=list(keys)).any())

def dedupe(df):
    """The frame without exact duplicate rows (first copy kept, index reset)."""
    return df.drop_duplicates().reset_index(drop=True)

def repeated_product_lines(df):
    """After dedupe: number of (InvoiceNo, StockCode) pairs that occur on more than one line."""
    lines = dedupe(df).groupby(["InvoiceNo", "StockCode"]).size()
    return int((lines > 1).sum())
