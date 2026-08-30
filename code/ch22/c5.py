# For this linear model, class weighting barely moves the ranking and
# destroys calibration. A tree ensemble can behave differently -- see the text.
plain = make_pipeline(StandardScaler(),
                      LogisticRegression(max_iter=5000)).fit(Xtr, ytr)
bal = make_pipeline(StandardScaler(),
                    LogisticRegression(max_iter=5000,
                                       class_weight="balanced")).fit(Xtr, ytr)

print(f"{'model':<12}{'AUC':>9}{'avg prec':>11}{'mean pred':>12}{'actual':>10}")
for name, m in [("plain", plain), ("balanced", bal)]:
    p = m.predict_proba(Xte)[:, 1]
    print(f"{name:<12}{roc_auc_score(yte, p):>9.4f}"
          f"{average_precision_score(yte, p):>11.4f}"
          f"{p.mean():>12.5f}{yte.mean():>10.5f}")

# Recalibrate the weighted model back onto the real scale.
cal = CalibratedClassifierCV(bal, method="isotonic", cv=5).fit(Xtr, ytr)
pc = cal.predict_proba(Xte)[:, 1]
print(f"{'recalibrated':<12}{roc_auc_score(yte, pc):>9.4f}"
      f"{average_precision_score(yte, pc):>11.4f}"
      f"{pc.mean():>12.5f}{yte.mean():>10.5f}")
