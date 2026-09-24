import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score
from sklearn.preprocessing import StandardScaler

def cluster_quality(df, k=4):
    """ari, silhouette and largest_cluster_share for k-means on the standardized features."""
    X = StandardScaler().fit_transform(df.drop(columns="TrueType"))
    labels = KMeans(n_clusters=k, n_init=10, random_state=0).fit_predict(X)
    return {
        "ari": float(adjusted_rand_score(df["TrueType"], labels)),
        "silhouette": float(silhouette_score(X, labels)),
        "largest_cluster_share": float(np.bincount(labels).max() / len(labels)),
    }
