# Boosting is not averaging. Each tree is fitted to what the ones before
# it got wrong, so the trees are deliberately dependent.
from sklearn.tree import DecisionTreeRegressor

f = np.zeros(len(Xtr))                    # running prediction, in log-odds
eta = 0.1
print(f"{'stage':>7}{'train log loss':>16}{'test AUC':>11}")
test_f = np.zeros(len(Xte))
for stage in range(1, 201):
    p = 1 / (1 + np.exp(-f))
    residual = ytr - p                     # gradient of log loss
    h = DecisionTreeRegressor(max_depth=3,
                              random_state=0).fit(Xtr, residual)
    f += eta * h.predict(Xtr)
    test_f += eta * h.predict(Xte)
    if stage in (1, 5, 25, 100, 200):
        pp = np.clip(1 / (1 + np.exp(-f)), 1e-9, 1 - 1e-9)
        ll = -np.mean(ytr*np.log(pp) + (1-ytr)*np.log(1-pp))
        print(f"{stage:>7}{ll:>16.4f}"
              f"{roc_auc_score(yte, test_f):>11.4f}")
