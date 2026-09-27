import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

df = pd.read_csv(data_path("retail.csv"))
df["Revenue"] = df.Quantity * df.UnitPrice
exp = df.groupby(["Country", "Category"]).Revenue.sum().unstack(fill_value=0).sort_index().sort_index(axis=1)
c = Checker("Q199 · Cross-tab with pivot_table", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.revenue_by_country_category(df.drop(columns="Revenue"))
c.check("rows are the countries, sorted", lambda: list(got.index) == list(exp.index) or f"index {list(got.index)}")
c.check("columns are the categories, sorted", lambda: list(got.columns) == list(exp.columns) or f"columns {list(got.columns)}")
c.check("cells are sums, not means", lambda: np.allclose(got.values, exp.values) or "values differ; pass aggfunc='sum'")
c.check("grand total equals total revenue", lambda: close(got.values.sum(), df.Revenue.sum(), 1e-6))
c.done()
