import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

df = pd.read_csv(data_path("customers.csv"))
yr = pd.to_datetime(df.SignupDate).dt.year
exp = pd.DataFrame({"customers": df.groupby(yr).size(), "churn_rate": df.Churn.groupby(yr).mean()})
c = Checker("Q203 · Churn by signup year", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.churn_by_signup_year(df)
c.check(f"index is the signup years {list(exp.index)}", lambda: [int(i) for i in got.index] == list(exp.index) or f"index {list(got.index)}")
c.check("columns are customers and churn_rate", lambda: list(got.columns) == ["customers", "churn_rate"] or f"columns {list(got.columns)}")
c.check("customers per year", lambda: list(got.customers) == list(exp.customers))
c.check("churn_rate per year", lambda: np.allclose(got.churn_rate, exp.churn_rate))
c.done()
