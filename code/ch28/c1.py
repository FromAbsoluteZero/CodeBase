import pandas as pd

s = pd.read_csv("daily_revenue.csv", parse_dates=["Date"])
s = s.set_index("Date")["Revenue"]

print(s.head(3))
print()
print(f"span:    {s.index.min().date()} to {s.index.max().date()}")
print(f"days:    {len(s):,}")
print(f"missing: {s.isna().sum()}")
print(f"gaps:    {(s.index.to_series().diff().dt.days > 1).sum()}")
