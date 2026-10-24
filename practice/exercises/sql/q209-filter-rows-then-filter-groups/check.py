import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

con = orders_connection()
df = pd.read_sql('SELECT * FROM orders', con)

b = df[df.Category == "Beans"].groupby("Country").Revenue.sum()
exp = b[b > 6000].sort_values(ascending=False).rename("BeansRevenue").reset_index()
c = Checker("Q209 · Filter rows, then filter groups", which_file(HERE, ".sql"))
got = run_sql_file(con, c.target)
c.check(f"{len(exp)} countries exceed 6,000 in Beans revenue, largest first", lambda: frame_equal(got, exp))
c.done()
