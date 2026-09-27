import shap
expl = shap.TreeExplainer(rf)
sv = expl.shap_values(Xte, check_additivity=False)[:, :, 1]

i = int(np.argmax(rf.predict_proba(Xte)[:, 1]))   # highest-risk person
base = expl.expected_value[1]
row = Xte.iloc[i]

print(f"employee {Xte.index[i]}   predicted risk "
      f"{rf.predict_proba(Xte)[i, 1]:.3f}   baseline {base:.3f}")
order = np.argsort(-np.abs(sv[i]))
for j in order:
    print(f"  {X.columns[j]:<22} = {row.iloc[j]:>8}   "
          f"pushes {sv[i, j]:>+.4f}")
print(f"  {'sum of pushes':<22}   {sv[i].sum():>+.4f}"
      f"   -> {base + sv[i].sum():.3f}")
