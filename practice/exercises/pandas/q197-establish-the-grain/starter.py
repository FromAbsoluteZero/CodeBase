import pandas as pd

def is_unique_grain(df, keys):
    """True if the columns in `keys` identify every row uniquely."""
    raise NotImplementedError

def dedupe(df):
    """The frame without exact duplicate rows (first copy kept, index reset)."""
    raise NotImplementedError

def repeated_product_lines(df):
    """After dedupe: number of (InvoiceNo, StockCode) pairs that occur on more than one line."""
    raise NotImplementedError
