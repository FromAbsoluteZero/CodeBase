import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

df = pd.read_csv(data_path("retail.csv"))
rev = df.Quantity * df.UnitPrice
canc = df.InvoiceNo.astype(str).str.startswith("C")
exp = pd.DataFrame({"Gross": rev[~canc].groupby(df.Category[~canc]).sum(), "Net": rev.groupby(df.Category).sum()}).sort_index()
c = Checker("Q201 · Cancellations, gross and net", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.gross_and_net(df)
c.check("index is the categories, sorted", lambda: list(got.index) == list(exp.index))
c.check("columns are Gross and Net", lambda: list(got.columns) == ["Gross", "Net"] or f"columns {list(got.columns)}")
c.check("Gross excludes cancellation lines", lambda: np.allclose(got.Gross, exp.Gross))
c.check("Net includes them (and is lower where cancellations occurred)", lambda: np.allclose(got.Net, exp.Net))
c.check("Net ≤ Gross for every category", lambda: bool((got.Net <= got.Gross + 1e-9).all()))
c.done()
