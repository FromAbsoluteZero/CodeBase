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
seg = pd.read_csv("segments.csv")
truth = seg.pop("TrueType").values
Xseg = StandardScaler().fit_transform(seg.values)
FEATS = list(seg.columns)
dig = load_digits()
Xd, yd = dig.data, dig.target
