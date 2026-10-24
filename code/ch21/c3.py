# Distances stop discriminating as dimensions grow. This is the reason
# kNN degrades on wide data, and it is arithmetic rather than folklore.
rng = np.random.default_rng(0)
print(f"{'dimensions':>11}{'nearest':>10}{'farthest':>10}"
      f"{'ratio':>9}{'contrast':>11}")
for d in (2, 5, 20, 100, 500):
    X = rng.uniform(size=(2000, d))
    q = rng.uniform(size=(1, d))
    dist = np.sqrt(((X - q) ** 2).sum(1))
    near, far = dist.min(), dist.max()
    print(f"{d:>11}{near:>10.3f}{far:>10.3f}{far/near:>9.2f}"
          f"{(far-near)/near:>11.3f}")
print("\nwhen the farthest point is barely further than the nearest,")
print("'nearest neighbour' has stopped meaning anything.")
