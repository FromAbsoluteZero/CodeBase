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
exp = pd.DataFrame({"Month": m.index, "Revenue": m.values, "RunningTotal": m.cumsum().values})
c = Checker("Q217 · Running total with a frame", which_file(HERE, ".sql"))
got = run_sql_file(con, c.target)
c.check("cumulative revenue by month", lambda: frame_equal(got, exp))
sql = c.target.read_text().upper()
c.check("the frame is stated with ROWS", lambda: "ROWS" in sql or "state the frame: ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW")
c.done()
