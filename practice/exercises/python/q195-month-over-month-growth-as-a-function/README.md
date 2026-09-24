# Q195 · Month-over-month growth as a function

Chapters 3 and 28 · intermediate · data: `data/generated/daily_revenue.csv`

`daily_revenue.csv` has one row per day (`Date`, `Revenue`) for 2023 and 2024. Write:

- `monthly_revenue(path)`: a dictionary mapping `YYYY-MM` to that month's total revenue.
- `mom_growth(monthly)`: given such a dictionary, return a dictionary mapping each month to its growth
  over the previous month as a fraction (`(this - previous) / previous`), with `None` for the first month.
  Months must be handled in chronological order whatever order the dictionary is in.

```bash
python practice/exercises/python/q195-month-over-month-growth-as-a-function/check.py
```
