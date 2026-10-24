# Q224 · Forecast baselines that must be beaten

Chapter 28 · intermediate · data: `data/generated/daily_revenue.csv`

Write `baseline_maes(df, horizon=90)` returning a dictionary with:

| key | value |
|---|---|
| `mean` | MAE over the last `horizon` days when every day is forecast as the mean of the training days |
| `naive` | MAE when every day is forecast as the last training day's revenue |
| `seasonal_naive` | MAE when day *t* of the holdout is forecast as the training day 7 days before it, cycling through the last training week |
| `best` | the key with the lowest MAE |

The training days are all days before the last `horizon` days, in date order.

```bash
python practice/exercises/challenges/q224-forecast-baselines-that-must-be-beaten/check.py
```
