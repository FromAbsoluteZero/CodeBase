# Q227 · Is the overtime effect real

Chapters 8, 15 and 42 · intermediate · data: `data/generated/hr.csv`

Write `overtime_effect(df)` returning a dictionary with:

| key | value |
|---|---|
| `rate_overtime`, `rate_no_overtime` | attrition rate in each group |
| `difference` | `rate_overtime - rate_no_overtime` |
| `ci_low`, `ci_high` | 95% confidence interval for the difference: `difference ± 1.96 × SE`, with `SE = sqrt(p1(1-p1)/n1 + p2(1-p2)/n2)` |
| `p_value` | two-sided p-value of the z-test with the pooled standard error `sqrt(p(1-p)(1/n1 + 1/n2))`, where `p` is the pooled rate |

Use the standard normal CDF from `scipy.stats.norm` or `math.erf`.

```bash
python practice/exercises/challenges/q227-is-the-overtime-effect-real/check.py
```
