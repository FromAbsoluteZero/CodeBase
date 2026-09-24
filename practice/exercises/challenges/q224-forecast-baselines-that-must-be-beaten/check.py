import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

df = pd.read_csv(data_path("daily_revenue.csv"))
s = df.sort_values("Date").Revenue.to_numpy(); tr, te = s[:-90], s[-90:]
seas = np.array([tr[-7:][i % 7] for i in range(90)])
exp = {"mean": np.abs(te - tr.mean()).mean(), "naive": np.abs(te - tr[-1]).mean(), "seasonal_naive": np.abs(te - seas).mean()}
best = min(exp, key=exp.get)
c = Checker("Q224 · Forecast baselines that must be beaten", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.baseline_maes(df)
for k, v in exp.items():
    c.check(f"{k} MAE = {v:.3f}", lambda k=k, v=v: close(got.get(k, float('nan')), v, 1e-6) or f"got {got.get(k)!r}")
c.check(f"best = {best}", lambda: got.get("best") == best or f"got {got.get('best')!r}")
c.done()
