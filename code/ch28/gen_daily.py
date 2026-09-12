import numpy as np, pandas as pd

rng = np.random.default_rng(11)
start = pd.Timestamp("2023-01-01")
days  = pd.date_range(start, periods=730, freq="D")

t     = np.arange(len(days))
trend = 1850 + 1.6 * t
dow   = np.array([1.00, 0.94, 0.97, 1.02, 1.18, 1.32, 0.86])
week  = dow[days.dayofweek]
year  = 1 + 0.16 * np.sin(2 * np.pi * (t - 80) / 365.25)
noise = rng.normal(1, 0.055, len(days))

rev = trend * week * year * noise
dec = (days.month == 12) & (days.day >= 10) & (days.day <= 24)
rev[dec] *= 1.45
closed = (days.month == 12) & (days.day == 25)
rev[closed] = 0

df = pd.DataFrame({"Date": days.strftime("%Y-%m-%d"),
                   "Revenue": rev.round(2)})
df.to_csv("daily_revenue.csv", index=False)
print(f"wrote daily_revenue.csv: {len(df):,} days, "
      f"{df.Date.min()} to {df.Date.max()}")
