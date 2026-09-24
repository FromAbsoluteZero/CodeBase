import pandas as pd

def bulk_beans_or_france(df):
    """Rows that are (Beans and Quantity >= 10) or France."""
    bulk_beans = (df["Category"] == "Beans") & (df["Quantity"] >= 10)
    france = df["Country"] == "France"
    return df[bulk_beans | france]
