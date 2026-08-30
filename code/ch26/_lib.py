import numpy as np, pandas as pd, warnings; warnings.filterwarnings("ignore")
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (silhouette_score, adjusted_rand_score,
                             calinski_harabasz_score)
df = pd.read_csv("segments.csv")
truth = df.pop("TrueType").values
FEATS = list(df.columns)
Xraw = df.values
X = StandardScaler().fit_transform(Xraw)
