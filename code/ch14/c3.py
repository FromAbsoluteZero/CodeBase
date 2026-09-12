from sklearn.metrics import confusion_matrix, accuracy_score

p = model.predict_proba(sc.transform(Xte))[:, 1]
pred = (p >= 0.5).astype(int)

cm = confusion_matrix(yte, pred)
tn, fp, fn, tp = cm.ravel()
print("                 predicted stay   predicted leave")
print(f"actually stayed  {tn:>14}{fp:>18}")
print(f"actually left    {fn:>14}{tp:>18}")

print(f"\nmodel accuracy:        {accuracy_score(yte, pred):.4f}")
print(f"'nobody leaves' accuracy: {1 - yte.mean():.4f}")
print(f"base rate (left):      {yte.mean():.4f}")
print(f"\nleavers found by the model:   {tp} of {tp + fn}")
print(f"leavers found by 'nobody leaves': 0 of {tp + fn}")
