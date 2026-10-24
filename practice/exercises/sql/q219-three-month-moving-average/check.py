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
exp = pd.DataFrame({"Month": m.index, "Revenue": m.values, "MovingAvg3": m.rolling(3, min_periods=1).mean().values})
c = Checker("Q219 · Three-month moving average", which_file(HERE, ".sql"))
got = run_sql_file(con, c.target)
c.check("moving average over this and the two previous months", lambda: frame_equal(got, exp))
c.done()
