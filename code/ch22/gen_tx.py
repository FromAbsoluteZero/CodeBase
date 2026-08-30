import numpy as np, pandas as pd
rng = np.random.default_rng(21)
n = 60000

amount = np.round(np.exp(rng.normal(3.4, 1.15, n)), 2)     # skewed, as money is
hour = rng.integers(0, 24, n)
age_days = np.clip(rng.gamma(2.0, 260, n), 1, 3000).round(0)
n_country = rng.choice([1, 2, 3], n, p=[0.88, 0.09, 0.03])
prior_chb = rng.poisson(0.06, n)

z = (-9.6
     + 0.95 * np.log1p(amount)
     + 1.60 * ((hour >= 1) & (hour <= 5))
     - 0.0032 * age_days
     + 1.45 * (n_country - 1)
     + 2.10 * prior_chb
     + rng.normal(0, 0.35, n))
fraud = (rng.random(n) < 1 / (1 + np.exp(-z))).astype(int)

pd.DataFrame({"Amount": amount, "Hour": hour, "AccountAgeDays": age_days,
              "CountriesUsed": n_country, "PriorChargebacks": prior_chb,
              "Fraud": fraud}).to_csv("transactions.csv", index=False)
print(f"wrote transactions.csv: {n:,} transactions, "
      f"{fraud.sum():,} fraudulent ({fraud.mean():.3%})")
