import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

con = orders_connection()
df = pd.read_sql('SELECT * FROM orders', con)

exp = pd.DataFrame({"RowsAfter": [len(df.drop_duplicates())]})
c = Checker("Q212 · Deduplicate with ROW_NUMBER", which_file(HERE, ".sql"))
got = run_sql_file(con, c.target)
c.check(f"RowsAfter = {len(df.drop_duplicates())}", lambda: frame_equal(got, exp))
c.done()
