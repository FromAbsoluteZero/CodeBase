"""Chapter 5, Step 3: a top-N running total must not include tied peers.

SQLite's default window frame for `SUM(rev) OVER (ORDER BY rev DESC)` is RANGE, which
includes every row tied with the current one, so a row ranked N by ROW_NUMBER() could carry
the revenue of more than N customers. The book's query now orders on a deterministic
tie-breaker and names the frame explicitly. Chapter 5 prints no companion directory, so the
corrected query is quoted here and run against a tie fixture and against the book's data.
"""
import sqlite3
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
BOOK_QUERY = """
    WITH clean AS (
        SELECT * FROM orders
        WHERE InvoiceNo NOT LIKE 'C%' AND CustomerID IS NOT NULL
    ),
    per_cust AS (
        SELECT CustomerID, SUM(Revenue) AS rev
        FROM clean GROUP BY CustomerID
    ),
    ranked AS (
        SELECT CustomerID, rev,
               ROW_NUMBER() OVER (ORDER BY rev DESC, CustomerID) AS rn,
               SUM(rev)     OVER (ORDER BY rev DESC, CustomerID
                                  ROWS UNBOUNDED PRECEDING) AS running,
               SUM(rev)     OVER ()                  AS grand
        FROM per_cust
    )
    SELECT rn AS top_n,
           ROUND(100.0 * running / grand, 1) AS pct_of_revenue
    FROM ranked
    WHERE rn IN (10, 25, 50, 100)
    ORDER BY rn
"""


def test_tie_fixture():
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE c(id INTEGER, rev REAL)")
    con.executemany("INSERT INTO c VALUES (?, ?)", [(1, 100), (2, 90), (3, 90), (4, 10)])
    default = con.execute("SELECT SUM(rev) OVER (ORDER BY rev DESC) FROM c ORDER BY rev DESC").fetchall()
    fixed = con.execute("SELECT SUM(rev) OVER (ORDER BY rev DESC, id ROWS UNBOUNDED PRECEDING) "
                        "FROM c ORDER BY rev DESC, id").fetchall()
    assert [r[0] for r in default] == [100, 280, 280, 290]     # the defect: rank 2 carries three customers
    assert [r[0] for r in fixed] == [100, 190, 280, 290]


def test_book_data_unchanged_by_the_fix():
    df = pd.read_csv(ROOT / "data" / "generated" / "retail.csv")
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    con = sqlite3.connect(":memory:"); df.to_sql("orders", con, index=False)
    got = pd.read_sql(BOOK_QUERY, con)
    assert got["pct_of_revenue"].tolist() == [8.1, 17.9, 31.3, 51.9]      # the printed table


if __name__ == "__main__":
    test_tie_fixture(); test_book_data_unchanged_by_the_fix(); print("ok")
