hr = pd.read_csv("hr.csv")
X = pd.get_dummies(hr.drop(columns="Attrition"),
                   columns=["Department", "OverTime"],
                   drop_first=True).astype(float)
y = hr["Attrition"].values
Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.3, random_state=7, stratify=y)
sc = StandardScaler().fit(Xtr)
model = LogisticRegression(max_iter=1000).fit(sc.transform(Xtr), ytr)
p = model.predict_proba(sc.transform(Xte))[:, 1]

print(f"training on {len(Xtr):,}, testing on {len(Xte):,}")
print(f"test base rate: {yte.mean():.1%}")
print(f"AUC: {roc_auc_score(yte, p):.4f}")
