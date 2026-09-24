import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

df = pd.read_csv(data_path("retail.csv"))
rev = df.Quantity * df.UnitPrice
exp = rev / rev.groupby(df.InvoiceNo).transform("sum")
c = Checker("Q204 · Share within group with transform", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.line_share(df)
c.check("a Series with one value per line, aligned to df", lambda: isinstance(got, pd.Series) and got.index.equals(df.index) or "return a Series aligned to df.index (use transform, not a merge that reorders)")
c.check("shares of each invoice sum to 1", lambda: np.allclose(got.groupby(df.InvoiceNo).sum(), 1.0))
c.check("values match", lambda: np.allclose(got, exp))
c.done()
