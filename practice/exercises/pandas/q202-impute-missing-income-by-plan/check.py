import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

df = pd.read_csv(data_path("customers.csv"))
miss = df.AnnualIncome.isna()
med = df.groupby("Plan").AnnualIncome.median()
c = Checker("Q202 · Impute missing income by plan", which_file(HERE, ".py"))
m = load_module(c.target)
out, n = m.fill_income_by_plan(df)
c.check(f"n_filled = {int(miss.sum())}", lambda: n == int(miss.sum()) or f"got {n}")
c.check("no missing income remains", lambda: out.AnnualIncome.notna().all())
c.check("filled rows carry their Plan's median", lambda: np.allclose(out.AnnualIncome[miss], df.Plan[miss].map(med)))
c.check("rows that had a value keep it", lambda: np.allclose(out.AnnualIncome[~miss], df.AnnualIncome[~miss]))
c.check("the input frame was not modified", lambda: df.AnnualIncome.isna().sum() == int(miss.sum()))
c.done()
