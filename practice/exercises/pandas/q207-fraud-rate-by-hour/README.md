# Q207 · Fraud rate by hour

Chapters 22 and 23 · beginner · data: `data/generated/transactions.csv`

Write:

- `base_rate(df)`: the share of transactions with `Fraud == 1`.
- `fraud_rate_by_hour(df)`: a DataFrame indexed by `Hour` (0 to 23) with columns `transactions`
  (count) and `fraud_rate`.
- `riskiest_hour(df)`: the hour with the highest fraud rate.

```bash
python practice/exercises/pandas/q207-fraud-rate-by-hour/check.py
```
