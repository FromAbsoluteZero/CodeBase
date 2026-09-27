# Is overtime really the best available split? Check every feature.
def entropy(p):
    return 0.0 if p in (0.0, 1.0) else -(p*np.log2(p) + (1-p)*np.log2(1-p))

def gain(col, thresh):
    left = Xtr[col].values <= thresh
    if left.sum() == 0 or (~left).sum() == 0:
        return 0.0
    w = sum(m.sum()/len(ytr) * entropy(ytr[m].mean()) for m in (left, ~left))
    return entropy(ytr.mean()) - w

print(f"{'feature':<22}{'best threshold':>16}{'gain':>9}")
best = []
for col in Xtr.columns:
    vals = np.unique(Xtr[col].values)
    cands = (vals[:-1] + vals[1:]) / 2 if len(vals) > 2 else [vals.mean()]
    g, t = max((gain(col, t), t) for t in cands)
    best.append((g, col, t))
    print(f"{col:<22}{t:>16.2f}{g:>9.4f}")
g, col, t = max(best)
print(f"\nwinner: {col} at {t:.2f}, gain {g:.4f}")
