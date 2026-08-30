# Chapter 19 claimed trees earn their advantage on interactions. Here is
# data with one: the outcome depends on whether two conditions AGREE,
# which no additive model can express.
r = np.random.default_rng(1)
n = 4000
a, b = r.normal(size=n), r.normal(size=n)
noise = r.normal(0, 1.1, n)
z = 1.1 * np.sign(a * b) + 0.4 * a + noise      # interaction dominates
yi = (z > 0).astype(int)
Xi = np.c_[a, b, r.normal(size=(n, 4))]         # plus four irrelevant columns

Xi_tr, Xi_te = Xi[:3000], Xi[3000:]
yi_tr, yi_te = yi[:3000], yi[3000:]

for name, m in [("logistic regression", make_pipeline(StandardScaler(),
                    LogisticRegression(max_iter=1000))),
                ("single tree (depth 4)", DecisionTreeClassifier(max_depth=4,
                    random_state=0)),
                ("random forest", RandomForestClassifier(n_estimators=300,
                    random_state=0)),
                ("gradient boosting", GradientBoostingClassifier(
                    n_estimators=200, learning_rate=0.05, random_state=0))]:
    m.fit(Xi_tr, yi_tr)
    pi = m.predict_proba(Xi_te)[:, 1]
    print(f"{name:<24}AUC {roc_auc_score(yi_te, pi):.4f}")
