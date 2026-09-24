import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

con = orders_connection()
df = pd.read_sql('SELECT * FROM orders', con)

d = df[df.CustomerID.notna()]
g = d.groupby("CustomerID").agg(Invoices=("InvoiceNo", "nunique"), Revenue=("Revenue", "sum")).reset_index()
exp = g[g.Invoices >= 5].sort_values("Revenue", ascending=False).reset_index(drop=True)
c = Checker("Q216 · Frequent customers", which_file(HERE, ".sql"))
got = run_sql_file(con, c.target)
c.check(f"{len(exp)} customers with five or more invoices, by revenue", lambda: frame_equal(got, exp, sort_by=["Revenue", "CustomerID"]))
c.done()
