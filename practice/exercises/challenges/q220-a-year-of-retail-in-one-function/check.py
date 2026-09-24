import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

df = pd.read_csv(data_path("retail.csv"))
rev = df.Quantity * df.UnitPrice; canc = df.InvoiceNo.astype(str).str.startswith("C")
monthly = rev.groupby(df.InvoiceDate.str[:7]).sum(); cat = rev.groupby(df.Category).sum()
ipc = df[df.CustomerID.notna()].groupby("CustomerID").InvoiceNo.nunique()
exp = {"net_revenue": rev.sum(), "cancellation_share": -rev[canc].sum() / rev[~canc].sum(),
       "best_month": monthly.idxmax(), "worst_month": monthly.idxmin(), "top_category": cat.idxmax(),
       "top_category_share": cat.max() / rev.sum(), "repeat_customer_share": (ipc > 1).mean()}
c = Checker("Q220 · A year of retail, in one function", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.retail_summary(df)
c.check("all seven keys", lambda: set(got) == set(exp) or f"keys {sorted(got)}")
for k, v in exp.items():
    if isinstance(v, str):
        c.check(f"{k} = {v}", lambda k=k, v=v: got.get(k) == v or f"got {got.get(k)!r}")
    else:
        c.check(f"{k} = {v:.4f}", lambda k=k, v=v: close(got.get(k, float('nan')), v, 1e-6) or f"got {got.get(k)!r}")
c.done()
