import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

con = orders_connection()
df = pd.read_sql('SELECT * FROM orders', con)

t = df.groupby("InvoiceNo").Revenue.sum()
second = sorted(t.unique(), reverse=True)[1]
exp = t[np.isclose(t, second)].rename("InvoiceTotal").reset_index()
c = Checker("Q211 · Second-highest invoice total", which_file(HERE, ".sql"))
got = run_sql_file(con, c.target)
c.check(f"the invoice(s) totalling {second:.2f}", lambda: frame_equal(got, exp, sort_by="InvoiceNo"))
c.done()
