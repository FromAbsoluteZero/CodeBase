import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(data_path("transactions.csv"))
X, y = df.drop(columns="Fraud"), df.Fraud
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, stratify=y, random_state=7)
prob = make_pipeline(StandardScaler(), LogisticRegression(class_weight="balanced", max_iter=1000)).fit(Xtr, ytr).predict_proba(Xte)[:, 1]
def at(t):
    pred = (prob >= t).astype(int); return precision_score(yte, pred, zero_division=0), recall_score(yte, pred)
pr, rc, th = precision_recall_curve(yte, prob); thr = th[np.flatnonzero(rc[:-1] >= 0.80)[-1]]
exp = {"base_rate": y.mean(), "precision_at_default": at(0.5)[0], "recall_at_default": at(0.5)[1], "threshold": thr, "precision_at_threshold": at(thr)[0], "recall_at_threshold": at(thr)[1]}
c = Checker("Q222 · Choosing a fraud threshold", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.fraud_threshold(df)
for k, v in exp.items():
    c.check(f"{k} = {v:.4f}", lambda k=k, v=v: close(got.get(k, float('nan')), v, 2e-3) or f"got {got.get(k)!r}")
c.check("recall at the chosen threshold is at least 0.80", lambda: got["recall_at_threshold"] >= 0.80 - 1e-9)
c.done()
