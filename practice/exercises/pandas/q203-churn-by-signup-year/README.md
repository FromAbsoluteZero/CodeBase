# Q203 · Churn by signup year

Chapters 11 and 12 · intermediate · data: `data/generated/customers.csv`

Write `churn_by_signup_year(df)` returning a DataFrame indexed by signup year (an integer) with two
columns: `customers`, the number of customers who signed up that year, and `churn_rate`, the share of them
with `Churn == 1`. `SignupDate` is text and must be parsed.

```bash
python practice/exercises/pandas/q203-churn-by-signup-year/check.py
```
