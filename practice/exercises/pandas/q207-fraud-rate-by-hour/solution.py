import pandas as pd

def base_rate(df):
    """Share of transactions that are fraud."""
    return float(df["Fraud"].mean())

def fraud_rate_by_hour(df):
    """Per hour: transactions and fraud_rate."""
    grouped = df.groupby("Hour")["Fraud"]
    return pd.DataFrame({"transactions": grouped.size(), "fraud_rate": grouped.mean()})

def riskiest_hour(df):
    """The hour with the highest fraud rate."""
    return int(fraud_rate_by_hour(df)["fraud_rate"].idxmax())
