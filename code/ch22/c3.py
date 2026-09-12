# ROC and PR describe the same model and disagree about how good it is.
m = make_pipeline(StandardScaler(),
                  LogisticRegression(max_iter=5000)).fit(Xtr, ytr)
p = m.predict_proba(Xte)[:, 1]

fpr, tpr, _ = roc_curve(yte, p)
prec, rec, _ = precision_recall_curve(yte, p)

# At the point where the model catches half the fraud:
i = np.argmin(np.abs(tpr - 0.5))
j = np.argmin(np.abs(rec - 0.5))
print(f"at 50% of fraud caught:")
print(f"  false positive rate {fpr[i]:.4f}   <- looks tiny")
print(f"  precision           {prec[j]:.4f}   <- the same point, honestly")
print(f"  flagged {int(fpr[i]*(len(yte)-yte.sum())+0.5*yte.sum()):,} "
      f"of {len(yte):,} to catch {int(0.5*yte.sum())} frauds")
print(f"\nROC AUC {roc_auc_score(yte, p):.4f}  "
      f"average precision {average_precision_score(yte, p):.4f}")
