import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

con = orders_connection()
df = pd.read_sql('SELECT * FROM orders', con)

per = df.groupby(["Country", "InvoiceNo"]).size().rename("Lines").reset_index()
exp = per.groupby("Country").agg(Invoices=("Lines", "size"), AvgLines=("Lines", "mean")).reset_index().sort_values("AvgLines", ascending=False).reset_index(drop=True)
c = Checker("Q215 · Average lines per invoice by country", which_file(HERE, ".sql"))
got = run_sql_file(con, c.target)
c.check("invoices and average lines per country, largest average first", lambda: frame_equal(got, exp))
c.done()
