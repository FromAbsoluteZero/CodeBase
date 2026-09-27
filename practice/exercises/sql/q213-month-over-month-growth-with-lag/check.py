import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

con = orders_connection()
df = pd.read_sql('SELECT * FROM orders', con)

m = df.groupby(df.InvoiceDate.str[:7]).Revenue.sum().sort_index()
exp = pd.DataFrame({"Month": m.index, "Revenue": m.values})
exp["PrevRevenue"] = exp.Revenue.shift(1)
exp["GrowthPct"] = (exp.Revenue - exp.PrevRevenue) / exp.PrevRevenue * 100
c = Checker("Q213 · Month-over-month growth with LAG", which_file(HERE, ".sql"))
got = run_sql_file(con, c.target)
c.check("twelve months, previous-month revenue and growth, NULL in the first row", lambda: frame_equal(got, exp))
c.done()
