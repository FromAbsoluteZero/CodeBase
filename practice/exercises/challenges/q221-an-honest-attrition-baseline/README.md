# Q221 · An honest attrition baseline

Chapters 14, 16 and 22 · intermediate · data: `data/generated/hr.csv`

Write `attrition_baseline(df)` returning a dictionary with:

| key | value |
|---|---|
| `majority_accuracy` | test-set accuracy of always predicting the majority class |
| `model_accuracy` | test-set accuracy of the model |
| `model_auc` | test-set ROC AUC of the model |

Use `train_test_split(test_size=0.2, stratify=y, random_state=42)`. The model is a `Pipeline`: a
`ColumnTransformer` that one-hot encodes `Department` and `OverTime` and standard-scales the numeric
columns, followed by `LogisticRegression(max_iter=1000)`. Fit it on the training rows only.

```bash
python practice/exercises/challenges/q221-an-honest-attrition-baseline/check.py
```
