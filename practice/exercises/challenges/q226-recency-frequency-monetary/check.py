import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

df = pd.read_csv(data_path("retail.csv"))
k = df[df.CustomerID.notna()].copy(); k["Rev"] = k.Quantity * k.UnitPrice; k["D"] = pd.to_datetime(k.InvoiceDate)
g = k.groupby("CustomerID").agg(last=("D", "max"), F=("InvoiceNo", "nunique"), M=("Rev", "sum"))
rec = (pd.Timestamp("2024-12-31") - g["last"]).dt.days
sc = lambda s, lab: pd.qcut(s.rank(method="first"), 4, labels=lab).astype(int)
R, F, M = sc(rec, [4, 3, 2, 1]), sc(g.F, [1, 2, 3, 4]), sc(g.M, [1, 2, 3, 4])
c = Checker("Q226 · Recency, frequency, monetary", which_file(HERE, ".py"))
m = load_module(c.target)
t = m.rfm(df)
c.check(f"one row per identified customer ({len(g)})", lambda: len(t) == len(g) and set(t.index) == set(g.index))
c.check("columns Recency, Frequency, Monetary, R, F, M", lambda: list(t.columns) == ["Recency", "Frequency", "Monetary", "R", "F", "M"] or f"columns {list(t.columns)}")
c.check("Recency in days to 2024-12-31", lambda: (t.Recency.loc[g.index].to_numpy() == rec.to_numpy()).all())
c.check("Frequency = distinct invoices", lambda: (t.Frequency.loc[g.index].to_numpy() == g.F.to_numpy()).all())
c.check("Monetary = net revenue", lambda: np.allclose(t.Monetary.loc[g.index], g.M))
c.check("R gives 4 to the most recent quartile", lambda: (t.R.loc[g.index].astype(int).to_numpy() == R.to_numpy()).all())
c.check("F and M give 4 to the highest quartile", lambda: (t.F.loc[g.index].astype(int).to_numpy() == F.to_numpy()).all() and (t.M.loc[g.index].astype(int).to_numpy() == M.to_numpy()).all())
n = int(((R + F + M) >= 10).sum())
c.check(f"top segment (R+F+M >= 10) has {n} customers", lambda: m.top_segment_count(t) == n or f"got {m.top_segment_count(t)}")
c.done()
