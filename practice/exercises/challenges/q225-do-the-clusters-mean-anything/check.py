import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from _checklib import *  # noqa: E402,F401
import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(data_path("segments.csv"))
X = StandardScaler().fit_transform(df.drop(columns="TrueType"))
lab = KMeans(n_clusters=4, n_init=10, random_state=0).fit_predict(X)
exp = {"ari": adjusted_rand_score(df.TrueType, lab), "silhouette": silhouette_score(X, lab), "largest_cluster_share": np.bincount(lab).max() / len(lab)}
c = Checker("Q225 · Do the clusters mean anything", which_file(HERE, ".py"))
m = load_module(c.target)
got = m.cluster_quality(df)
for k, v in exp.items():
    c.check(f"{k} = {v:.4f}", lambda k=k, v=v: close(got.get(k, float('nan')), v, 1e-3) or f"got {got.get(k)!r}")
c.done()
