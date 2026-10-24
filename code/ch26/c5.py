# k-means assumes clusters are round blobs of similar size. When they are
# not, it fails in a way no choice of k repairs.
from sklearn.datasets import make_moons
Xm, ym = make_moons(n_samples=1200, noise=0.06, random_state=0)
Xm = StandardScaler().fit_transform(Xm)

def ward(k):
    return AgglomerativeClustering(k, linkage="ward").fit_predict(Xm)
def single(k):
    return AgglomerativeClustering(k, linkage="single").fit_predict(Xm)

runs = [("k-means (k=2)",
         KMeans(2, n_init=10, random_state=0).fit_predict(Xm)),
        ("hierarchical (ward)", ward(2)),
        ("hierarchical (single)", single(2)),
        ("DBSCAN", DBSCAN(eps=0.30, min_samples=8).fit_predict(Xm))]

for name, lab in runs:
    n = len(set(lab)) - (1 if -1 in lab else 0)
    print(f"{name:<24}clusters {n}   "
          f"ARI {adjusted_rand_score(ym, lab):.3f}")
print("\nthe two moons are the same size and equally dense --")
print("only the SHAPE defeats k-means.")
