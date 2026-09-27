bal = LogisticRegression(max_iter=1000,
                        class_weight="balanced")
bal.fit(sc.transform(Xtr), ytr)
pb = bal.predict_proba(sc.transform(Xte))[:, 1]

for name, probs in [("unweighted", p), ("balanced", pb)]:
    pr = (probs >= 0.5).astype(int)
    tn, fp, fn, tp = confusion_matrix(yte, pr).ravel()
    print(f"{name:<12} at threshold 0.5: "
          f"flagged {tp+fp:>3}, caught {tp:>2} of {tp+fn}, "
          f"AUC {roc_auc_score(yte, probs):.3f}")

print(f"\nmean predicted probability, unweighted: {p.mean():.3f}")
print(f"mean predicted probability, balanced:   {pb.mean():.3f}")
print(f"true base rate:                         {yte.mean():.3f}")
