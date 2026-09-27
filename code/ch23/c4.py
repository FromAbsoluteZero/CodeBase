# Does the theoretical p* actually minimize cost on held-out data?
m = make_pipeline(StandardScaler(),
                  LogisticRegression(max_iter=5000)).fit(Xtr, ytr)
pr = m.predict_proba(Xte)[:, 1]
p_star = C_FP / (C_FP + C_FN)

def cost(th):
    pred = pr >= th
    return (C_FP * int((pred & (yte == 0)).sum())
            + C_FN * int((~pred & (yte == 1)).sum()))

grid = np.unique(np.round(np.geomspace(0.0005, 0.5, 400), 6))
costs = np.array([cost(t) for t in grid])
best = grid[costs.argmin()]

print(f"theoretical p*        {p_star:.4f}   cost {cost(p_star):>9,.0f}")
print(f"empirical minimum     {best:.4f}   cost {costs.min():>9,.0f}")
print(f"default 0.50          0.5000   cost {cost(0.5):>9,.0f}")
print(f"flag everything       0.0000   cost {cost(0.0):>9,.0f}")
print(f"flag nothing          1.0000   cost {C_FN*yte.sum():>9,.0f}")
print(f"\nusing p* rather than the empirical optimum costs "
      f"{cost(p_star) - costs.min():,.0f} more")
