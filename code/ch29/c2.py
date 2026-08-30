imp = pd.Series(rf.feature_importances_,
                index=X.columns).sort_values(ascending=False)
print("impurity importance, straight from the forest")
for k, v in imp.items():
    print(f"  {k:<22} {v:.3f}")
