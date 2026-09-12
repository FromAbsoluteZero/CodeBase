def entropy(p):
    if p in (0.0, 1.0):
        return 0.0
    return -(p * np.log2(p) + (1 - p) * np.log2(1 - p))

H_parent = entropy(ytr.mean())
print(f"parent: n={len(ytr)}  p={ytr.mean():.4f}  H={H_parent:.4f}")

ot = Xtr["OverTime_Yes"].values == 1
weighted = 0.0
for label, mask in [("OverTime=Yes", ot), ("OverTime=No", ~ot)]:
    p_child = ytr[mask].mean()
    h = entropy(p_child)
    weighted += mask.sum() / len(ytr) * h
    print(f"  {label:<13} n={mask.sum():>4}  p={p_child:.4f}  H={h:.4f}")

print(f"weighted child entropy {weighted:.4f}")
print(f"information gain       {H_parent - weighted:.4f}")
