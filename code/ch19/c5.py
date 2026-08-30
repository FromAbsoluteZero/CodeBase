t = DecisionTreeClassifier(max_depth=3, random_state=0).fit(Xtr, ytr)
print(export_text(t, feature_names=list(Xtr.columns), decimals=1))
