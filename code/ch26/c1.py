# Scaling is not optional here. k-means minimizes squared distance, so a
# column measured in larger numbers dominates the geometry.
print(f"{'feature':<16}{'mean':>10}{'std':>10}{'range':>12}")
for i, f in enumerate(FEATS):
    c = Xraw[:, i]
    print(f"{f:<16}{c.mean():>10.1f}{c.std():>10.1f}"
          f"{c.max() - c.min():>12.1f}")

for label, data in [("unscaled", Xraw), ("standardized", X)]:
    km = KMeans(4, n_init=10, random_state=0).fit(data)
    print(f"\n{label:<13} ARI against the true types: "
          f"{adjusted_rand_score(truth, km.labels_):.3f}")
