import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

df = pd.read_csv(data_path("retail.csv"))
c = Checker("Q198 · Merge with a contract", which_file(HERE, ".py"))
m = load_module(c.target)
t = m.invoice_totals(df)
c.check("one row per invoice", lambda: len(t) == df.InvoiceNo.nunique() and t.InvoiceNo.is_unique)
exp = (df.Quantity * df.UnitPrice).groupby(df.InvoiceNo).sum()
c.check("InvoiceTotal is the sum of Quantity × UnitPrice", lambda: np.allclose(t.set_index("InvoiceNo").loc[exp.index, "InvoiceTotal"], exp))
out = m.add_invoice_total(df)
c.check("row count unchanged after the merge", lambda: len(out) == len(df) or f"{len(out)} rows; the merge multiplied or dropped rows")
c.check("every line carries its invoice's total", lambda: np.allclose(out.InvoiceTotal, out.InvoiceNo.map(exp)))
bad = pd.concat([t, t.iloc[:1]])
def refuses():
    try:
        m.add_invoice_total(df, bad)
    except pd.errors.MergeError:
        return True
    return "the merge accepted a right table with a duplicated key; pass validate='m:1'"
c.check("a duplicated right key makes the merge raise MergeError", refuses)
c.done()
