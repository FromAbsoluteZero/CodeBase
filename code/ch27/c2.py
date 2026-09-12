# 64 pixels per digit. How many directions does that really occupy?
Xs = StandardScaler().fit_transform(Xd)
p = PCA().fit(Xs)
cum = np.cumsum(p.explained_variance_ratio_)
print(f"{len(Xd):,} images, {Xd.shape[1]} pixels each")
for target in (0.50, 0.80, 0.90, 0.95, 0.99):
    k = int(np.searchsorted(cum, target) + 1)
    print(f"  {target:.0%} of the variance needs {k:>2} components "
          f"({k/Xd.shape[1]:.0%} of the columns)")
