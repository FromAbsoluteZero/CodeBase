# Chapter 26 clustered in the original space. Does reducing first help?
cases = [("original 4 features", Xseg)]
for k in (2, 3):
    cases.append((f"PCA, {k} components",
                  PCA(n_components=k, random_state=0).fit_transform(Xseg)))
for name, data in cases:
    km = KMeans(4, n_init=10, random_state=0).fit(data)
    print(f"{name:<22} ARI {adjusted_rand_score(truth, km.labels_):.3f}")

# And on the digits, where the original space is much larger.
Xs = StandardScaler().fit_transform(Xd)
for name, data in [("original 64 pixels", Xs),
                   ("PCA, 10 components",
                    PCA(n_components=10, random_state=0).fit_transform(Xs)),
                   ("PCA, 20 components",
                    PCA(n_components=20, random_state=0).fit_transform(Xs))]:
    km = KMeans(10, n_init=10, random_state=0).fit(data)
    print(f"{name:<22} ARI {adjusted_rand_score(yd, km.labels_):.3f}")
