# SQL and data manipulation

Still the single most reliably tested skill in data roles, and the one most often failed on nerves rather than knowledge.

Track: SQL · 22 questions · [All topics](README.md) · [Practice home](../README.md)

Levels: beginner 9, intermediate 12, advanced 1. Types: conceptual 6, coding 15, scenario 1.

Answer each question aloud before you open its note.

<a id="q9"></a>

**Q9.** Explain the difference between INNER, LEFT, and FULL OUTER JOIN.

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

Inner keeps only matching rows; left keeps all left rows with nulls where no match exists; full outer keeps unmatched rows from both sides. Watch for row multiplication when the join key is not unique.

</details>

<a id="q10"></a>

**Q10.** What is a window function, and when would you use one instead of GROUP BY?

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

It computes across a set of rows while preserving row-level detail. Use it for running totals, rankings, and period-over-period comparisons where collapsing rows would lose the information you need.

</details>

<a id="q11"></a>

**Q11.** Write a query to find the second highest salary in a table.

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

<details>
<summary>What a strong answer contains</summary>

Common approaches: DENSE_RANK in a subquery filtered to rank 2, or a correlated subquery on the max below the overall max. Strong answers ask whether ties should count as one rank.

</details>

<a id="q12"></a>

**Q12.** How would you find and remove duplicate rows?

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

<details>
<summary>What a strong answer contains</summary>

Identify duplicates with ROW_NUMBER partitioned by the key columns, then delete or filter rows where the number exceeds one. First clarify what duplicate means, since exact and business-key duplicates differ.

</details>

<a id="q13"></a>

**Q13.** A query that ran in two seconds now takes four minutes. How do you diagnose it?

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; advanced &nbsp;·&nbsp; scenario</sub>

> **Beyond the book.** Execution plans and indexes are not taught in this book; Chapter 5 teaches the SQL itself. Your database's documentation on EXPLAIN is the place to start.

<details>
<summary>What a strong answer contains</summary>

Read the execution plan, check for missing or unused indexes, look for full scans and spilled sorts, check whether data volume or statistics changed, and confirm no implicit type conversion is defeating an index.

</details>

<a id="q14"></a>

**Q14.** WHERE or HAVING — how do you decide?

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

WHERE filters rows before grouping, HAVING filters groups after aggregation. Strong answers note that anything expressible in WHERE belongs there, because filtering before the aggregation is both correct and cheaper.

</details>

<a id="q15"></a>

**Q15.** Why can you not filter on a column alias in WHERE?

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

WHERE is evaluated before SELECT, so the alias does not yet exist. Strong answers give the logical order of evaluation — FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY — and note that ORDER BY can use the alias precisely because it runs last.

</details>

<a id="q16"></a>

**Q16.** Why does WHERE x = NULL return nothing?

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

NULL means unknown, and any comparison with an unknown is unknown rather than true, so no row qualifies. Strong answers give IS NULL as the fix and mention that the same logic makes NOT IN behave unexpectedly when the subquery contains a NULL.

</details>

<a id="q17"></a>

**Q17.** What is a CTE and when would you use one?

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; conceptual</sub>

<details>
<summary>What a strong answer contains</summary>

A named subquery defined with WITH, readable in sequence rather than nested inside out. Strong answers cite readability and reuse within one statement, and note that recursive CTEs handle hierarchies; a candidate who claims CTEs are always faster is guessing.

</details>

<a id="q18"></a>

**Q18.** How would you compute month-over-month growth?

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

<details>
<summary>What a strong answer contains</summary>

Aggregate to month, then compare each month against the previous with a window function such as LAG. Strong answers mention guarding against division by zero and against gaps — a missing month makes LAG compare across a hole and report growth that never happened.

</details>

<a id="q208"></a>

**Q208.** Write the query that returns total revenue per category, highest first.

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; coding</sub>

Exercise: [sql/q208-revenue-by-category](../exercises/sql/q208-revenue-by-category/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

GROUP BY Category with SUM(Revenue), aliased, and ORDER BY that alias descending. ORDER BY runs last, so it can see the alias; WHERE could not (Q15). Strong solutions know that the six clauses run FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, whatever order they are written in.

</details>

<a id="q209"></a>

**Q209.** List the countries whose revenue from Beans exceeds 6,000, using WHERE for the rows and HAVING for the groups.

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; coding</sub>

Exercise: [sql/q209-filter-rows-then-filter-groups](../exercises/sql/q209-filter-rows-then-filter-groups/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

WHERE Category = 'Beans' keeps only the bean lines before grouping; HAVING SUM(Revenue) > 6000 keeps only the countries whose total qualifies after it. Putting the category test in HAVING would work but would aggregate every line first, which is slower and muddles intent (Q14). Strong solutions put every condition that can go in WHERE there.

</details>

<a id="q210"></a>

**Q210.** For each category, return its top product by revenue, using ROW_NUMBER in a CTE.

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [sql/q210-best-selling-product-per-category](../exercises/sql/q210-best-selling-product-per-category/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

Aggregate to (Category, Description) first, then ROW_NUMBER() OVER (PARTITION BY Category ORDER BY Revenue DESC) in a CTE, and filter rn = 1 in the outer query. The filter cannot go in the same SELECT's WHERE because window functions are evaluated after WHERE (Q12). Strong solutions say what happens on ties and add a tiebreaker to the ORDER BY.

</details>

<a id="q211"></a>

**Q211.** Find the invoice with the second-highest total revenue, using DENSE_RANK so that ties are handled.

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [sql/q211-second-highest-invoice-total](../exercises/sql/q211-second-highest-invoice-total/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

Aggregate to one row per invoice, rank with DENSE_RANK() OVER (ORDER BY total DESC) in a CTE, and select rank 2. DENSE_RANK rather than ROW_NUMBER, so two invoices tied for first both rank 1 and the second-highest value is still rank 2; LIMIT 1 OFFSET 1 gets that wrong under ties (Q11).

</details>

<a id="q212"></a>

**Q212.** Count the rows that remain after exact duplicates are removed, using ROW_NUMBER over every column.

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [sql/q212-deduplicate-with-row-number](../exercises/sql/q212-deduplicate-with-row-number/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

PARTITION BY every column in a CTE, keep rn = 1 in the outer query, then count. The rn filter must sit outside the CTE, because WHERE runs before window functions are computed; the version that puts ROW_NUMBER() = 1 directly in WHERE does not run (Q12). Strong solutions mention that SELECT DISTINCT answers this particular question too, and that ROW_NUMBER is the tool when you must choose which copy to keep.

</details>

<a id="q213"></a>

**Q213.** Compute each month's revenue, the previous month's revenue, and the growth between them.

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [sql/q213-month-over-month-growth-with-lag](../exercises/sql/q213-month-over-month-growth-with-lag/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

Aggregate to months in a CTE with substr(InvoiceDate, 1, 7), then LAG(Revenue) OVER (ORDER BY Month) gives the previous row's value; growth is (Revenue - Prev) / Prev, NULL for the first month because LAG returns NULL there (Q18). Strong solutions guard against a zero previous month and note that LAG assumes no month is missing from the data.

</details>

<a id="q214"></a>

**Q214.** Count all rows, the rows with a customer, and the rows without one, in a single query.

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; beginner &nbsp;·&nbsp; coding</sub>

Exercise: [sql/q214-counting-with-nulls](../exercises/sql/q214-counting-with-nulls/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

COUNT(*) counts rows; COUNT(CustomerID) counts non-NULL values, so the difference is the missing ones, or SUM(CASE WHEN CustomerID IS NULL THEN 1 ELSE 0 END) counts them directly. WHERE CustomerID = NULL finds nothing, because nothing equals NULL; IS NULL is the test (Q16). Strong solutions say why COUNT(column) and COUNT(*) differ.

</details>

<a id="q215"></a>

**Q215.** Compute the average number of order lines per invoice in each country, aggregating in two steps.

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [sql/q215-average-lines-per-invoice-by-country](../exercises/sql/q215-average-lines-per-invoice-by-country/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

First a CTE with one row per invoice and its line count, then AVG over that per country. Averaging directly over the line-level table would weight each invoice by its own number of lines, which is the grain error again (Q7). Strong solutions state the grain of each step.

</details>

<a id="q216"></a>

**Q216.** List the customers with at least five invoices, with their invoice count and total revenue.

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [sql/q216-frequent-customers](../exercises/sql/q216-frequent-customers/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

Exclude NULL customers in WHERE, group by CustomerID, COUNT(DISTINCT InvoiceNo) for invoices because the grain is order lines, SUM(Revenue) for spend, HAVING on the distinct count. Strong solutions say why COUNT(*) would be wrong here and why the NULL customers must be excluded rather than grouped as one giant customer.

</details>

<a id="q217"></a>

**Q217.** Compute the cumulative revenue month by month with a window frame stated explicitly.

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [sql/q217-running-total-with-a-frame](../exercises/sql/q217-running-total-with-a-frame/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

SUM(Revenue) OVER (ORDER BY Month ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW). Chapter 5 insists on the ROWS frame: without it, the default frame is RANGE, and rows with tied ORDER BY values are added together, which gives a different running total whenever the ordering column repeats. Strong solutions can say what the default frame is and when it bites.

</details>

<a id="q218"></a>

**Q218.** Report each month's gross revenue (cancellations excluded) and net revenue (cancellations included) in one query.

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [sql/q218-gross-and-net-by-month-with-case](../exercises/sql/q218-gross-and-net-by-month-with-case/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

A conditional sum: SUM(CASE WHEN InvoiceNo NOT LIKE 'C%' THEN Revenue ELSE 0 END) for gross beside a plain SUM(Revenue) for net, both in one GROUP BY. Two queries joined would work but doubles the scan. Strong solutions say which figure each stakeholder wants.

</details>

<a id="q219"></a>

**Q219.** Compute a three-month moving average of monthly revenue with a bounded window frame.

<sub>Chapters [5](../by-chapter/ch05.md) &nbsp;·&nbsp; intermediate &nbsp;·&nbsp; coding</sub>

Exercise: [sql/q219-three-month-moving-average](../exercises/sql/q219-three-month-moving-average/) · data: `retail.csv`

<details>
<summary>What a strong answer contains</summary>

AVG(Revenue) OVER (ORDER BY Month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) after aggregating to months in a CTE. The first two months average over fewer rows; strong solutions say so, and either accept it or return NULL there with a COUNT() OVER the same frame. This is the same frame clause as the running total with different bounds (Q10).

</details>

---

<sub>Question and answer text © 2026 Shanmukh Behara, licensed under [CC BY-NC-SA 4.0](../../LICENSES/CC-BY-NC-SA-4.0.txt). It is not covered by the MIT licence that applies to the code. See [LICENSING.md](../../LICENSING.md).</sub>
