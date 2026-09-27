import numpy as np
rng = np.random.default_rng(0)
pop = orders["rev"].values

print(f"population: mean {pop.mean():.2f} "
      f"sd {pop.std(ddof=1):.2f} skew {pd.Series(pop).skew():.2f}")
print()
for k in [1, 5, 30]:
    means = [rng.choice(pop, k).mean() for _ in range(5000)]
    print(f"  n={k:>2}: mean {np.mean(means):7.2f}  "
          f"sd {np.std(means, ddof=1):6.2f}  "
          f"skew {pd.Series(means).skew():5.2f}")

print(f"\npredicted sd at n=30 = sd/sqrt(30) = "
      f"{pop.std(ddof=1) / np.sqrt(30):.2f}")
