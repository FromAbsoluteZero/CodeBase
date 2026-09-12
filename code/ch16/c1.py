hr = pd.read_csv("hr.csv")
X = pd.get_dummies(hr.drop(columns="Attrition"),
                   columns=["Department", "OverTime"],
                   drop_first=True).astype(float)
y = hr["Attrition"].values

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3,
                                      random_state=7, stratify=y)
print(f"train {len(Xtr):,}  test {len(Xte):,}")
print(f"base rate: train {ytr.mean():.4f}  test {yte.mean():.4f}")
print("the test set is now closed until the final step")
