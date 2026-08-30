p_star = C_FP / (C_FP + C_FN)

def total_cost(pred):
    fp = int(((pred == 1) & (yte == 0)).sum())
    fn = int(((pred == 0) & (yte == 1)).sum())
    return C_FP * fp + C_FN * fn, fp, fn

print(f"{'model':<10}{'threshold':>11}{'recall':>9}{'precision':>11}"
      f"{'FP':>7}{'FN':>5}{'cost':>10}")
for name, kw in [("plain", {}), ("weighted", {"class_weight": "balanced"})]:
    m = make_pipeline(StandardScaler(),
                      LogisticRegression(max_iter=5000, **kw)).fit(Xtr, ytr)
    pr = m.predict_proba(Xte)[:, 1]
    for th, lab in [(0.5, "0.50 default"), (p_star, f"{p_star:.4f} p*")]:
        pred = (pr >= th).astype(int)
        c, fp, fn = total_cost(pred)
        print(f"{name:<10}{lab:>11}{recall_score(yte, pred):>9.3f}"
              f"{precision_score(yte, pred, zero_division=0):>11.3f}"
              f"{fp:>7}{fn:>5}{c:>10,.0f}")
print(f"\nheld-out set: {len(yte):,} transactions, {yte.sum()} fraudulent")
print(f"cost of flagging nothing at all: {C_FN * yte.sum():>10,.0f}")
