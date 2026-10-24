import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

con = orders_connection()
df = pd.read_sql('SELECT * FROM orders', con)

exp = pd.DataFrame({"TotalRows": [len(df)], "WithCustomer": [int(df.CustomerID.notna().sum())], "WithoutCustomer": [int(df.CustomerID.isna().sum())]})
c = Checker("Q214 · Counting with NULLs", which_file(HERE, ".sql"))
got = run_sql_file(con, c.target)
c.check(f"{len(df)} rows, {int(df.CustomerID.notna().sum())} with a customer, {int(df.CustomerID.isna().sum())} without", lambda: frame_equal(got, exp))
c.done()
