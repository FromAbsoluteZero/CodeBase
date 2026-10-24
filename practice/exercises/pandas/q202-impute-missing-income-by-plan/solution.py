import pandas as pd

def fill_income_by_plan(df):
    """(copy of df with AnnualIncome gaps filled by the Plan median, number of values filled)."""
    out = df.copy()
    missing = out["AnnualIncome"].isna()
    plan_median = out.groupby("Plan")["AnnualIncome"].transform("median")
    out["AnnualIncome"] = out["AnnualIncome"].fillna(plan_median)
    return out, int(missing.sum())
