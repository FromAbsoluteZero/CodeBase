import numpy as np, pandas as pd, warnings; warnings.filterwarnings("ignore")
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (silhouette_score, adjusted_rand_score,
                             calinski_harabasz_score)
# segments.csv is created by this chapter's Step 1, gen_seg.py. The blocks read it from the
# working directory exactly as the book does; if it is not here yet, use the copy shipped in
# data/generated/ (byte-identical to what the generator writes).
import os as _os, shutil as _shutil
if not _os.path.exists("segments.csv"):
    for _d in ("../../data/generated", "../data/generated", "data/generated"):
        if _os.path.exists(_os.path.join(_d, "segments.csv")):
            _shutil.copy(_os.path.join(_d, "segments.csv"), "segments.csv"); break
df = pd.read_csv("segments.csv")
truth = df.pop("TrueType").values
FEATS = list(df.columns)
Xraw = df.values
X = StandardScaler().fit_transform(Xraw)
