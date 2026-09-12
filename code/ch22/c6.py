# The threshold is a business decision. Price both errors and sweep.
REVIEW = 6.0          # analyst time per flagged transaction
LOSS = 240.0          # average loss on a fraud that gets through
CATCH = 0.85          # ASSUMPTION: review stops 85% of the fraud it sees

m = make_pipeline(StandardScaler(),
                  LogisticRegression(max_iter=5000)).fit(Xtr, ytr)
p = m.predict_proba(Xte)[:, 1]

print(f"break-even precision: {REVIEW / (LOSS * CATCH):.2%}")
print(f"\n{'thresh':>8}{'flagged':>9}{'caught':>8}{'review $':>11}"
      f"{'loss saved $':>14}{'net $':>10}")
best = None
for th in (0.30, 0.10, 0.05, 0.02, 0.01, 0.005, 0.002):
    pred = p >= th
    tp = int(((pred) & (yte == 1)).sum())
    cost = pred.sum() * REVIEW
    saved = tp * LOSS * CATCH
    net = saved - cost
    best = max(best or (net, th), (net, th))
    print(f"{th:>8.3f}{pred.sum():>9}{tp:>8}{cost:>11,.0f}"
          f"{saved:>14,.0f}{net:>10,.0f}")
print(f"\nbest net value at threshold {best[1]}: ${best[0]:,.0f}")
