# Q222 · Choosing a fraud threshold

Chapters 22 and 23 · advanced · data: `data/generated/transactions.csv`

Write `fraud_threshold(df, required_recall=0.80)` returning a dictionary with:

| key | value |
|---|---|
| `base_rate` | share of fraud in the whole file |
| `precision_at_default`, `recall_at_default` | precision and recall on the test set at threshold 0.5 |
| `threshold` | the **highest** threshold (from the test-set probabilities) whose recall is at least `required_recall` |
| `precision_at_threshold`, `recall_at_threshold` | precision and recall at that threshold |

Use `train_test_split(test_size=0.25, stratify=y, random_state=7)`, a `Pipeline` of `StandardScaler`
and `LogisticRegression(class_weight="balanced", max_iter=1000)`, and consider every distinct predicted
probability on the test set as a candidate threshold (`precision_recall_curve` does exactly that).

```bash
python practice/exercises/challenges/q222-choosing-a-fraud-threshold/check.py
```
