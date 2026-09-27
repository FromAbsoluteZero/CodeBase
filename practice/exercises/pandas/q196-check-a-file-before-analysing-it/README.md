# Q196 · Check a file before analysing it

Chapters 4 and 11 · beginner · data: `data/generated/retail.csv`

Interview question Q6 asks how you would check a file before analysing it. Write `profile(df)` that
takes a DataFrame and returns a dictionary with these keys:

| key | value |
|---|---|
| `rows` | number of rows |
| `columns` | list of column names, in order |
| `null_counts` | dict of column → number of missing values, **only** for columns that have any |
| `duplicate_rows` | number of rows that are exact duplicates of an earlier row |
| `date_min`, `date_max` | earliest and latest `InvoiceDate` as `YYYY-MM-DD` strings |

```bash
python practice/exercises/pandas/q196-check-a-file-before-analysing-it/check.py
```
