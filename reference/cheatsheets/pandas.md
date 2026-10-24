# pandas cheat sheet

Chapter 4 teaches everything here, and Chapter 11 builds on it. The grain of a table, what one row
represents, is the thing to establish before any of it.

| Task | Idiom | Chapter |
|---|---|---|
| Look at it first | `df.shape` · `df.head()` · `df.dtypes` · `df.describe()` · `df.isna().sum()` | 4, 11 |
| Select by label / position | `df.loc[rows, cols]` · `df.iloc[i, j]` | 4 |
| Filter rows | `df[df["col"] > 5]` · combine conditions with `&` and `\|`, and wrap **each condition in parentheses**: `df[(df["a"] > 5) & (df["b"] == "x")]` | 4 |
| Modify a filtered result | A filter returns a new frame (pandas 3 copies; it never writes through to the original). To change the original, assign with `.loc`: `df.loc[mask, "col"] = value` | 4 |
| New column | `df["new"] = df["a"] / df["b"]` — vectorized, no loop | 4 |
| Group and aggregate | `df.groupby("k").agg(total=("x", "sum"), n=("x", "size"))` | 4 |
| Group and keep every row | `df.groupby("k")["x"].transform("sum")` — aligned to the original rows, so a share within group is `df["x"] / that` | 4 |
| Join | `a.merge(b, on="key", how="left", validate="m:1")` — `validate` raises if the right key is not unique; compare `len()` before and after | 4 |
| Sort | `df.sort_values("col", ascending=False)` | 4 |
| Counts | `df["col"].value_counts(dropna=False)` | 4 |
| Missing values | `df["col"].fillna(value)` · `df.dropna(subset=["col"])` · fill by group: `df["col"].fillna(df.groupby("k")["col"].transform("median"))` | 11 |
| Duplicates | `df.duplicated().sum()` · `df.drop_duplicates()` · `df.duplicated(subset=keys).any()` tests whether `keys` are a grain | 11 |
| Dates | `pd.to_datetime(df["d"])` then `.dt.year`, `.dt.month`, `.dt.dayofweek` · `df.set_index("d").resample("W").mean()` | 11, 28 |
| Long → wide | `df.pivot_table(values="x", index="r", columns="c", aggfunc="sum", fill_value=0)` — **name `aggfunc`**; the default is the mean | 4 |
| Wide → long | `df.melt(id_vars=["k"], var_name="col", value_name="x")` | 4 |
| Read / write | `pd.read_csv(path)` · `df.to_csv(path, index=False)` | 4 |

**The mistake that costs most:** a merge that silently multiplies rows because the key is not unique
on the side you assumed. `validate="m:1"` turns it into an error; comparing `len(df)` before and after
catches it when you forgot.

Practise: [Q196](../../practice/by-topic/python-pandas-data.md#q196) to
[Q207](../../practice/by-topic/python-pandas-data.md#q207) in the exercises.

---

<sub>© 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt); see [LICENSING.md](../../LICENSING.md). Corrections: [docs/ERRATA.md](../../docs/ERRATA.md). Every snippet was checked against the versions pinned in `requirements.txt` (pandas 3.0.2, scikit-learn 1.8.0).</sub>
