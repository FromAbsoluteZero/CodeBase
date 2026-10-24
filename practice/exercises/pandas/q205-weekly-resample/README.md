# Q205 · Weekly resample

Chapter 28 · beginner · data: `data/generated/daily_revenue.csv`

Write:

- `weekly_mean(df)`: a Series of mean daily revenue per calendar week (weeks ending Sunday, pandas'
  default for `"W"`), indexed by the week-ending date.
- `best_week(df)`: a tuple `(week_ending, mean_revenue)` for the week with the highest mean.

```bash
python practice/exercises/pandas/q205-weekly-resample/check.py
```
