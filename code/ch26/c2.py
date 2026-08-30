# Choosing k. Inertia always falls, so it cannot pick k on its own.
print(f"{'k':>3}{'inertia':>12}{'silhouette':>13}{'Calinski-H':>13}{'ARI':>8}")
for k in range(2, 9):
    km = KMeans(k, n_init=10, random_state=0).fit(X)
    print(f"{k:>3}{km.inertia_:>12,.0f}"
          f"{silhouette_score(X, km.labels_):>13.3f}"
          f"{calinski_harabasz_score(X, km.labels_):>13.0f}"
          f"{adjusted_rand_score(truth, km.labels_):>8.3f}")
print("\nthe true answer is 4 clusters plus 200 customers in none of them")
