print(f"{'thresh':>7}{'flagged':>9}{'TP':>5}{'FP':>5}{'FN':>5}"
      f"{'precision':>11}{'recall':>9}{'F1':>8}")
for th in [0.50, 0.30, 0.20, 0.15]:
    pr = (p >= th).astype(int)
    tn, fp, fn, tp = confusion_matrix(yte, pr).ravel()
    prec = tp / (tp + fp) if tp + fp else 0
    rec = tp / (tp + fn)
    f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0
    print(f"{th:>7.2f}{tp+fp:>9}{tp:>5}{fp:>5}{fn:>5}"
          f"{prec:>11.3f}{rec:>9.3f}{f1:>8.3f}")
