# SQL cheat sheet

Written order and execution order are different, which is the source of most confusing errors.
Chapter 5 works through why. Examples use the `orders` table Chapter 5 builds from `retail.csv`.

| Task | Idiom | Chapter |
|---|---|---|
| Written order | `SELECT · FROM · WHERE · GROUP BY · HAVING · ORDER BY` | 5 |
| Execution order | `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY` | 5 |
| Filter rows / groups | `WHERE` filters rows before grouping; `HAVING` filters groups after. Anything that can go in `WHERE` belongs there | 5 |
| Aggregates | `COUNT(*)` · `COUNT(col)` · `SUM` · `AVG` · `MIN` · `MAX` | 5 |
| `COUNT(*)` vs `COUNT(col)` | `COUNT(*)` counts rows; `COUNT(col)` skips NULLs | 5 |
| NULL | NULL is never equal to anything, including NULL. Use `IS NULL` / `IS NOT NULL` | 5 |
| Conditional aggregation | `SUM(CASE WHEN status = 'paid' THEN amount ELSE 0 END)` | 5 |
| Joins | `INNER` keeps matches · `LEFT` keeps all of the left side · check the grain of both sides, or the join multiplies rows | 5 |
| CTE | `WITH step1 AS (...) SELECT ... FROM step1` — readable beats nested | 5 |
| Window function | `SUM(x) OVER (PARTITION BY k ORDER BY d ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)` — aggregates without collapsing rows. **State the `ROWS` frame**: the default frame is `RANGE`, which adds tied `ORDER BY` values together | 5 |
| Previous row | `LAG(x) OVER (ORDER BY d)` · next row `LEAD(x)` · NULL where there is none | 5 |
| Moving average | `AVG(x) OVER (ORDER BY d ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)` | 5 |
| Ranking | `ROW_NUMBER()` · `RANK()` · `DENSE_RANK()` `OVER (PARTITION BY k ORDER BY x DESC)` | 5 |
| Deduplicate | Number the copies in a CTE, then filter outside it: `WITH r AS (SELECT *, ROW_NUMBER() OVER (PARTITION BY key ORDER BY updated DESC) AS rn FROM t) SELECT * FROM r WHERE rn = 1`. A window function cannot be filtered in the same query's `WHERE` | 5 |
| Second highest | `DENSE_RANK() OVER (ORDER BY x DESC)` in a CTE, then `WHERE rnk = 2`; ties are handled, which `LIMIT 1 OFFSET 1` gets wrong | 5 |
| Alias in `WHERE` | A column alias created in `SELECT` cannot be used in `WHERE`, because `SELECT` runs after `WHERE`. Repeat the expression, or wrap it in a CTE | 5 |

Practise: [Q208](../../practice/by-topic/sql.md#q208) to [Q219](../../practice/by-topic/sql.md#q219),
each with a check that runs your query against the same table.

---

<sub>© 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt); see [LICENSING.md](../../LICENSING.md). Corrections: [docs/ERRATA.md](../../docs/ERRATA.md). Every snippet was checked against the versions pinned in `requirements.txt` (pandas 3.0.2, scikit-learn 1.8.0).</sub>
