# t-SNE preserves neighbourhoods, not distances. It is a viewing tool.
import time
Xs = StandardScaler().fit_transform(Xd)
pca2 = PCA(n_components=2, random_state=0).fit_transform(Xs)

t0 = time.perf_counter()
ts2 = TSNE(n_components=2, init="pca", perplexity=30,
           random_state=0).fit_transform(Xs)
t_tsne = time.perf_counter() - t0

# How well does each 2-D view separate the ten digits? Cluster the
# view and see how far the clusters agree with the true labels.
views = [("PCA (2 components)", pca2),
         ("t-SNE (2 dimensions)", ts2)]
for name, emb in views:
    lab = KMeans(10, n_init=10, random_state=0).fit_predict(emb)
    ari = adjusted_rand_score(yd, lab)
    print(f"{name:<24} ARI against the true digit {ari:.3f}")

print(f"\nt-SNE took {t_tsne:.1f}s for {len(Xd):,} points, and cannot")
print("transform new points -- there is no .transform() to call.")
