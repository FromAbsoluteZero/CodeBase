from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict

# 1,200 tickets from 30 agents, 40 each. Each agent has a hidden tendency
# to escalate. Every ticket also carries its agent's fingerprint: eight
# arbitrary numbers (desk, shift, tooling) that are fixed for that agent and
# say nothing about the tendency. Only the evidence varies ticket by ticket.
rng = np.random.default_rng(0)
agent = np.repeat(np.arange(30), 40)              # the repeated entity
tendency = rng.normal(0, 1, 30)[agent]            # hidden, never a feature
finger = rng.normal(0, 1, (30, 8))[agent]         # arbitrary, repeated
evidence = rng.normal(0, 1, (len(agent), 2))      # the real evidence
logit = tendency + 0.6 * evidence[:, 0] + 0.3 * evidence[:, 1]
yg = (rng.random(len(agent)) < 1 / (1 + np.exp(-logit))).astype(int)
Xg = np.c_[evidence, finger]

forest = RandomForestClassifier(300, min_samples_leaf=5, random_state=0)
splits = {"random": (StratifiedKFold(5, shuffle=True, random_state=0), None),
          "grouped": (GroupKFold(5), agent)}   # six whole agents per fold
for name, (sp, g) in splits.items():
    p = cross_val_predict(forest, Xg, yg, groups=g, cv=sp,
                          method="predict_proba")[:, 1]
    folds = [roc_auc_score(yg[te], p[te]) for _, te in sp.split(Xg, yg, g)]
    print(f"{name:<8} 5-fold  pooled AUC {roc_auc_score(yg, p):.3f}"
          f"   folds {min(folds):.3f} to {max(folds):.3f}")

new = agent >= 24                     # six agents the model never sees
forest.fit(Xg[~new], yg[~new])
p_new = forest.predict_proba(Xg[new])[:, 1]
print(f"six new agents held out   AUC {roc_auc_score(yg[new], p_new):.3f}")
