# Q186 · Count rows and sum a column

Chapters 3 and 4 · beginner · data: `data/generated/retail.csv`

Using only the standard library, write two functions in `starter.py`:

- `row_count(path)` returns the number of data rows in the file (the header is not a row).
- `total_quantity(path)` returns the sum of the `Quantity` column as an integer.

Use `csv.DictReader`. Remember that everything a CSV reader gives you is text.

Check your work from the repository root:

```bash
python practice/exercises/python/q186-count-rows-and-sum-a-column/check.py
```
