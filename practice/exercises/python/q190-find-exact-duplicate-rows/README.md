# Q190 · Find exact duplicate rows

Chapter 11 · intermediate · data: `data/generated/retail.csv`

Some rows in `retail.csv` are exact duplicates: every column identical. Write:

- `duplicate_rows(path)`: a list of the distinct rows that occur more than once, each as a tuple of its
  column values in file order, each listed once, in the order they first appear in the file.
- `extra_copies(path)`: how many rows would be removed if every duplicate were kept once.

```bash
python practice/exercises/python/q190-find-exact-duplicate-rows/check.py
```
