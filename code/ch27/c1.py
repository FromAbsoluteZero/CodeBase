# PCA finds directions of maximum variance. On four correlated behavioural
# measures, how much of the picture lives in how few directions?
p = PCA().fit(Xseg)
print(f"{'component':>10}{'variance':>11}{'cumulative':>13}")
for i, (v, c) in enumerate(zip(p.explained_variance_ratio_,
                               np.cumsum(p.explained_variance_ratio_)), 1):
    print(f"{i:>10}{v:>11.3f}{c:>13.3f}")

print(f"\nloadings: what each component is made of")
print(f"{'feature':<16}" + "".join(f"{'PC'+str(i+1):>9}" for i in range(4)))
for j, f in enumerate(FEATS):
    print(f"{f:<16}" + "".join(f"{p.components_[i, j]:>9.2f}"
                               for i in range(4)))
