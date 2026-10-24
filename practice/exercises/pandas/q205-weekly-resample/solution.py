import pandas as pd

def weekly_mean(df):
    """Mean daily Revenue per week, indexed by week-ending date."""
    daily = df.assign(Date=pd.to_datetime(df["Date"])).set_index("Date")["Revenue"]
    return daily.resample("W").mean()

def best_week(df):
    """(week_ending Timestamp, mean revenue) for the best week."""
    weekly = weekly_mean(df)
    return weekly.idxmax(), float(weekly.max())
