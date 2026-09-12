rows = []
for th in np.arange(0.05, 0.55, 0.05):
    pr = (p >= th).astype(int)
    tn, fp, fn, tp = confusion_matrix(yte, pr).ravel()
    spend = (tp + fp) * call_cost
    saved = tp * success * replace_cost
    rows.append({"th": round(th, 2), "flagged": tp + fp, "tp": tp,
                 "precision": round(tp/(tp+fp), 3) if tp+fp else 0,
                 "spend": spend, "saved": round(saved),
                 "net": round(saved - spend)})
res = pd.DataFrame(rows)
print(res.to_string(index=False))
