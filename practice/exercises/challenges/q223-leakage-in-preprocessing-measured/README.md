# Q223 · Leakage in preprocessing, measured

Chapters 16, 24 and 25 · intermediate · data: `data/generated/customers.csv`

Write `leakage_comparison(df)` returning a dictionary with:

| key | value |
|---|---|
| `honest_auc` | mean 5-fold ROC AUC of a `Pipeline(SimpleImputer(median), StandardScaler, LogisticRegression(max_iter=1000))` |
| `leaky_auc` | mean 5-fold ROC AUC when the imputer and scaler are fitted on **all** rows first and only the classifier is cross-validated |
| `gap` | `leaky_auc - honest_auc` |

Features are the four numeric columns `AnnualIncome`, `Sessions`, `AvgBasket` and the signup age in days
(days from `SignupDate` to 2024-12-31); the target is `Churn`. Use
`StratifiedKFold(n_splits=5, shuffle=True, random_state=0)` for both runs.

```bash
python practice/exercises/challenges/q223-leakage-in-preprocessing-measured/check.py
```
