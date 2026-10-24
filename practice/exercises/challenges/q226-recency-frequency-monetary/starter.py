import pandas as pd

def rfm(df, as_of="2024-12-31"):
    """RFM table indexed by CustomerID with Recency, Frequency, Monetary, R, F, M."""
    raise NotImplementedError

def top_segment_count(rfm_table):
    """Number of customers whose R + F + M is at least 10."""
    raise NotImplementedError
