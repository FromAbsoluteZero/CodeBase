import numpy as np, pandas as pd
rng = np.random.default_rng(24)
n = 8000

city = rng.choice([f"CITY_{i:03d}" for i in range(180)], n)      # high cardinality
plan = rng.choice(["basic", "plus", "pro"], n, p=[.55, .32, .13])
channel = rng.choice(["web", "app", "phone"], n, p=[.5, .38, .12])
signup = pd.to_datetime("2023-01-01") + pd.to_timedelta(
    rng.integers(0, 730, n), unit="D")
income = np.round(np.exp(rng.normal(10.2, 0.55, n)), 0)
sessions = rng.poisson(6, n)
basket = np.round(np.exp(rng.normal(3.1, 0.7, n)), 2)

# churn depends on plan, engagement, and value-for-money -- not on city
z = (-0.4
     - 0.55 * (plan == "pro") + 0.35 * (plan == "basic")
     - 0.09 * sessions
     + 1.85 * (basket / (income / 1000) > 1.4)
     + 0.30 * (channel == "phone")
     + rng.normal(0, 0.6, n))
churn = (rng.random(n) < 1 / (1 + np.exp(-z))).astype(int)

df = pd.DataFrame({"City": city, "Plan": plan, "Channel": channel,
                   "SignupDate": signup.strftime("%Y-%m-%d"),
                   "AnnualIncome": income, "Sessions": sessions,
                   "AvgBasket": basket, "Churn": churn})
df.loc[rng.random(n) < 0.09, "AnnualIncome"] = np.nan     # real gaps
df.to_csv("customers.csv", index=False)
print(f"wrote customers.csv: {n:,} customers, churn {churn.mean():.1%}, "
      f"{df.City.nunique()} cities, {df.AnnualIncome.isna().sum()} missing incomes")
