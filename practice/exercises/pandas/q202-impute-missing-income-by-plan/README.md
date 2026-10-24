# Q202 · Impute missing income by plan

Chapters 11 and 24 · intermediate · data: `data/generated/customers.csv`

`AnnualIncome` is missing for some customers. Write `fill_income_by_plan(df)` returning a tuple
`(filled_frame, n_filled)`: a copy of the frame in which each missing `AnnualIncome` is replaced by the
median income of customers on the same `Plan`, and the number of values filled. Do not modify the frame
you were given.

```bash
python practice/exercises/pandas/q202-impute-missing-income-by-plan/check.py
```
