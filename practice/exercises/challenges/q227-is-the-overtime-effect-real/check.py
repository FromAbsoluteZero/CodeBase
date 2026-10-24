import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

from scipy.stats import norm

df = pd.read_csv(data_path("hr.csv"))
a, b = df[df.OverTime == "Yes"].Attrition, df[df.OverTime == "No"].Attrition
p1, p2, n1, n2 = a.mean(), b.mean(), len(a), len(b); d = p1 - p2
se = np.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2); pp = (a.sum() + b.sum()) / (n1 + n2)
z = d / np.sqrt(pp * (1 - pp) * (1 / n1 + 1 / n2)); pv = 2 * norm.sf(abs(z))
exp = {"rate_overtime": p1, "rate_no_overtime": p2, "difference": d, "ci_low": d - 1.96 * se, "ci_high": d + 1.96 * se, "p_value": pv}
c = Checker("Q227 · Is the overtime effect real", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.overtime_effect(df)
for k, v in exp.items():
    tol = 1e-6 if k != "p_value" else 1e-9
    c.check(f"{k} = {v:.6g}", lambda k=k, v=v, tol=tol: close(got.get(k, float('nan')), v, tol) or f"got {got.get(k)!r}")
c.done()
