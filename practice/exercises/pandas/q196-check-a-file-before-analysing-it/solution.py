import pandas as pd

def profile(df):
    """A dictionary describing the frame: rows, columns, null_counts, duplicate_rows, date_min, date_max."""
    nulls = df.isna().sum()
    dates = pd.to_datetime(df["InvoiceDate"])
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "null_counts": {col: int(n) for col, n in nulls.items() if n > 0},
        "duplicate_rows": int(df.duplicated().sum()),
        "date_min": dates.min().strftime("%Y-%m-%d"),
        "date_max": dates.max().strftime("%Y-%m-%d"),
    }
