import numpy as np, pandas as pd, warnings; warnings.filterwarnings("ignore")
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, roc_auc_score
from sklearn.model_selection import cross_val_score, StratifiedKFold, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
# segments.csv is created by Chapter 26 (code/ch26/gen_seg.py). The blocks read it from the
# working directory exactly as the book does; if it is not here yet, use the copy shipped in
# data/generated/ (byte-identical to what the generator writes).
import os as _os, shutil as _shutil
if not _os.path.exists("segments.csv"):
    for _d in ("../../data/generated", "../data/generated", "data/generated"):
        if _os.path.exists(_os.path.join(_d, "segments.csv")):
            _shutil.copy(_os.path.join(_d, "segments.csv"), "segments.csv"); break
seg = pd.read_csv("segments.csv")
truth = seg.pop("TrueType").values
Xseg = StandardScaler().fit_transform(seg.values)
FEATS = list(seg.columns)
dig = load_digits()
Xd, yd = dig.data, dig.target
