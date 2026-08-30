# Cost is not the only constraint. Capacity usually binds first.
m = make_pipeline(StandardScaler(),
                  LogisticRegression(max_iter=5000)).fit(Xtr, ytr)
pr = m.predict_proba(Xte)[:, 1]
p_star = C_FP / (C_FP + C_FN)

CAPACITY = 200        # reviews this team can actually do
order = np.argsort(-pr)
top = order[:CAPACITY]
flagged_by_pstar = int((pr >= p_star).sum())

print(f"threshold p* would flag       {flagged_by_pstar:,} transactions")
print(f"the team can review           {CAPACITY}")
print(f"implied threshold at capacity {pr[order[CAPACITY-1]]:.4f}")
print()
print(f"reviewing the top {CAPACITY}: caught {yte[top].sum()} of {yte.sum()}"
      f"   precision {yte[top].mean():.1%}")
net = yte[top].sum() * C_FN - CAPACITY * C_FP
print(f"net value {net:,.0f}   versus {C_FN*yte.sum():,.0f} of loss "
      f"if nothing is reviewed")
