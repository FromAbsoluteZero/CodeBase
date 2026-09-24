import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

con = orders_connection()
df = pd.read_sql('SELECT * FROM orders', con)

mo = df.InvoiceDate.str[:7]; canc = df.InvoiceNo.astype(str).str.startswith("C")
exp = pd.DataFrame({"Month": sorted(mo.unique())})
exp["Gross"] = exp.Month.map(df[~canc].groupby(mo[~canc]).Revenue.sum())
exp["Net"] = exp.Month.map(df.groupby(mo).Revenue.sum())
c = Checker("Q218 · Gross and net by month with CASE", which_file(HERE, ".sql"))
got = run_sql_file(con, c.target)
c.check("gross and net per month", lambda: frame_equal(got, exp))
c.done()
