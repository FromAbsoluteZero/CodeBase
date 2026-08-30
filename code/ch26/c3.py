# Three algorithms, same data, same scaling.
km = KMeans(4, n_init=10, random_state=0).fit(X)
hc = AgglomerativeClustering(4, linkage="ward").fit(X)
db = DBSCAN(eps=0.55, min_samples=12).fit(X)

for name, lab in [("k-means (k=4)", km.labels_),
                  ("hierarchical (ward)", hc.labels_),
                  ("DBSCAN", db.labels_)]:
    n_found = len(set(lab)) - (1 if -1 in lab else 0)
    noise = int((lab == -1).sum())
    sil = silhouette_score(X[lab != -1], lab[lab != -1]) if n_found > 1 else 0
    print(f"{name:<22} clusters {n_found}   noise {noise:>4}   "
          f"ARI {adjusted_rand_score(truth, lab):.3f}   sil {sil:.3f}")

# Only DBSCAN can decline to assign a point. How good is it at that?
flagged = db.labels_ == -1
real_noise = truth == "unclassifiable"
print(f"\nof {flagged.sum()} points DBSCAN called noise, "
      f"{int((flagged & real_noise).sum())} were genuinely unclassifiable")
print(f"of {real_noise.sum()} genuinely unclassifiable customers, "
      f"DBSCAN caught {int((flagged & real_noise).sum())}")
