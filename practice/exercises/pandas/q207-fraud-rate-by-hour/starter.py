import pandas as pd

def base_rate(df):
    """Share of transactions that are fraud."""
    raise NotImplementedError

def fraud_rate_by_hour(df):
    """Per hour: transactions and fraud_rate."""
    raise NotImplementedError

def riskiest_hour(df):
    """The hour with the highest fraud rate."""
    raise NotImplementedError
