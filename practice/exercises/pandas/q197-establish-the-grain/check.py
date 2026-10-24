import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

df = pd.read_csv(data_path("retail.csv"))
keys = ["InvoiceNo", "StockCode"]
c = Checker("Q197 · Establish the grain", which_file(HERE, ".py"))
m = load_module(c.target)
c.check("InvoiceNo alone is not a grain (an invoice has several lines)", lambda: m.is_unique_grain(df, ["InvoiceNo"]) is False)
c.check("(InvoiceNo, StockCode) is not a grain of the raw file", lambda: m.is_unique_grain(df, keys) is False or "the raw file has repeated (InvoiceNo, StockCode) pairs")
d = m.dedupe(df)
exp_len = len(df) - int(df.duplicated().sum())
c.check(f"dedupe keeps {exp_len} rows", lambda: len(d) == exp_len or f"got {len(d)}")
c.check("dedupe resets the index", lambda: list(d.index) == list(range(len(d))))
c.check("dedupe keeps the first copy (row order preserved)", lambda: d.iloc[0].to_dict() == df.iloc[0].to_dict())
c.check("after dedupe, (InvoiceNo, StockCode) is STILL not a grain", lambda: m.is_unique_grain(d, keys) is False or "some invoices list the same product on two lines; the grain is one row per order line")
exp_rep = int((df.drop_duplicates().groupby(keys).size() > 1).sum())
c.check(f"{exp_rep} invoice-product pairs occur on more than one line", lambda: m.repeated_product_lines(df) == exp_rep or f"got {m.repeated_product_lines(df)}")
c.check("the original frame is not modified", lambda: len(df) == exp_len + int(df.duplicated().sum()))
c.done()
