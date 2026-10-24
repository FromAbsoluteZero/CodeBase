import pandas as pd

def attrition_table(df):
    """Department × OverTime table of attrition rates."""
    return df.pivot_table(values="Attrition", index="Department", columns="OverTime", aggfunc="mean")

def riskiest(df):
    """(Department, OverTime) with the highest attrition rate."""
    stacked = attrition_table(df).stack()
    return tuple(stacked.idxmax())
