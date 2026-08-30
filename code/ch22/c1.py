m = make_pipeline(StandardScaler(),
                  LogisticRegression(max_iter=5000)).fit(Xtr, ytr)
p = m.predict_proba(Xte)[:, 1]

print(f"held-out transactions: {len(yte):,}   fraudulent: {yte.sum()} "
      f"({yte.mean():.3%})")
pred = (p >= 0.5).astype(int)
tn, fp, fn, tp = confusion_matrix(yte, pred).ravel()
print(f"\nat the default threshold of 0.5:")
print(f"  flagged {pred.sum()}   caught {tp} of {yte.sum()}")
print(f"  accuracy {(tn + tp) / len(yte):.4f}")
print(f"  accuracy of flagging nothing at all: {1 - yte.mean():.4f}")
print(f"\nROC AUC          {roc_auc_score(yte, p):.4f}")
print(f"average precision {average_precision_score(yte, p):.4f}")
print(f"a random model    0.5000 ROC AUC, {yte.mean():.4f} avg precision")
