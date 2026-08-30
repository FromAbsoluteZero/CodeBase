import numpy as np, pandas as pd
rng = np.random.default_rng(11)
n = 1470
tenure   = np.clip(rng.gamma(2.2, 3.0, n), 0.2, 40).round(1)
salary   = np.clip(rng.normal(65000, 18000, n), 25000, 160000).round(-2)
overtime = (rng.random(n) < 0.28).astype(int)
commute  = np.clip(rng.gamma(2.0, 6.0, n), 1, 60).round(0)
satis    = np.clip(rng.normal(3.3, 0.95, n), 1, 5).round(1)
promo    = np.clip(rng.gamma(1.6, 1.6, n), 0, 15).round(1)
dept     = rng.choice(["Sales", "R&D", "Support"], n, p=[0.32, 0.45, 0.23])
z = (-2.55 + 1.15*overtime - 0.135*tenure - 0.60*(satis - 3.3)
     + 0.024*commute + 0.095*promo - 0.000014*(salary - 65000)
     + np.where(dept == "Sales", 0.45,
                np.where(dept == "Support", 0.20, 0.0)))
left = (rng.random(n) < 1 / (1 + np.exp(-z))).astype(int)
hr = pd.DataFrame({"Department": dept, "YearsAtCompany": tenure,
    "MonthlyIncome": (salary/12).round(0),
    "OverTime": np.where(overtime == 1, "Yes", "No"),
    "CommuteMinutes": commute, "JobSatisfaction": satis,
    "YearsSincePromotion": promo, "Attrition": left})
hr.to_csv("hr.csv", index=False)
print(f"{len(hr):,} employees, attrition rate {hr['Attrition'].mean():.1%}")
