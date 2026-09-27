import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

con = orders_connection()
df = pd.read_sql('SELECT * FROM orders', con)

p = df.groupby(["Category", "Description"]).Revenue.sum().reset_index()
exp = (p.sort_values(["Category", "Revenue", "Description"], ascending=[True, False, True])
         .groupby("Category").head(1).sort_values("Category").reset_index(drop=True))
c = Checker("Q210 · Best-selling product per category", which_file(HERE, ".sql"))
got = run_sql_file(con, c.target)
c.check("one row per category with its top product", lambda: frame_equal(got, exp))
c.done()
