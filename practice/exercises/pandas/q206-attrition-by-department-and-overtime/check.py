import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

df = pd.read_csv(data_path("hr.csv"))
exp = df.groupby(["Department", "OverTime"]).Attrition.mean().unstack()
c = Checker("Q206 · Attrition by department and overtime", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.attrition_table(df)
c.check("rows are departments", lambda: sorted(got.index) == sorted(exp.index) or f"index {list(got.index)}")
c.check("columns are No and Yes", lambda: sorted(got.columns) == ["No", "Yes"] or f"columns {list(got.columns)}")
c.check("cells are rates (means of the 0/1 outcome)", lambda: np.allclose(got.loc[exp.index, exp.columns].values, exp.values))
r = m.riskiest(df)
e = exp.stack().idxmax()
c.check(f"riskiest is {e}", lambda: tuple(r) == tuple(e) or f"got {r}")
c.done()
