import pandas as pd

def churn_by_signup_year(df):
    """Per signup year: customers and churn_rate."""
    year = pd.to_datetime(df["SignupDate"]).dt.year
    grouped = df.groupby(year)["Churn"]
    return pd.DataFrame({"customers": grouped.size(), "churn_rate": grouped.mean()}).rename_axis("year")
