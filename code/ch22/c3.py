# ROC and PR describe the same model and disagree about how good it is.
m = make_pipeline(StandardScaler(),
                  LogisticRegression(max_iter=5000)).fit(Xtr, ytr)
p = m.predict_proba(Xte)[:, 1]

fpr, tpr, thr = roc_curve(yte, p)
# every number below is read at one threshold from this curve

# At the point where the model catches half the fraud:
i = np.argmin(np.abs(tpr - 0.5))
flag = p >= thr[i]; prec = yte[flag].mean()
print(f"at 50% of fraud caught:")
print(f"  false positive rate {fpr[i]:.4f}   <- looks tiny")
print(f"  precision           {prec:.4f}   <- the same point, honestly")
print(f"  flagged {flag.sum():,} "
      f"of {len(yte):,} to catch {yte[flag].sum()} frauds")
print(f"\nROC AUC {roc_auc_score(yte, p):.4f}  "
      f"average precision {average_precision_score(yte, p):.4f}")
