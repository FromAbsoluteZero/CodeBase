import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

con = orders_connection()
df = pd.read_sql('SELECT * FROM orders', con)

exp = df.groupby("Category").Revenue.sum().sort_values(ascending=False).rename("Revenue").reset_index()
c = Checker("Q208 · Revenue by category", which_file(HERE, ".sql"))
got = run_sql_file(con, c.target)
c.check("one row per category, columns Category and Revenue, largest first", lambda: frame_equal(got, exp))
c.done()
