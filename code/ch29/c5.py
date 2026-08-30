import shap

expl = shap.TreeExplainer(rf)
sv = expl.shap_values(Xte, check_additivity=False)[:, :, 1]   # class 1

mean_abs = pd.Series(np.abs(sv).mean(0),
                     index=X.columns).sort_values(ascending=False)
print("mean |SHAP| — average size of each feature's contribution")
for k, v in mean_abs.items():
    print(f"  {k:<22} {v:.4f}")
