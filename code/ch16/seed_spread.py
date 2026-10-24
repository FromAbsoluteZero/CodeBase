# Step 5's numbers depend on the random draw, so this re-runs c5.py
# unchanged except for the data seed, over five seeds (0 to 4) fixed before
# any result was seen. For each seed it also scores the model, fitted on all
# 30 agents, on 300 brand-new agents drawn from the same process: a large
# new-agent sample that shows which of the estimates is close to the truth.
#   python seed_spread.py
import numpy as np
from sklearn.model_selection import StratifiedKFold, GroupKFold
from sklearn.metrics import roc_auc_score


def tickets(rng, n_agents, per=40):
    """The generator in c5.py, for any number of agents."""
    agent = np.repeat(np.arange(n_agents), per)
    tendency = rng.normal(0, 1, n_agents)[agent]
    finger = rng.normal(0, 1, (n_agents, 8))[agent]
    evidence = rng.normal(0, 1, (len(agent), 2))
    logit = tendency + 0.6 * evidence[:, 0] + 0.3 * evidence[:, 1]
    y = (rng.random(len(agent)) < 1 / (1 + np.exp(-logit))).astype(int)
    return np.c_[evidence, finger], y


src = open("c5.py", encoding="utf-8").read()
assert src.count("default_rng(0)") == 1
for seed in range(5):
    print(f"seed {seed}")
    ns = {"np": np, "StratifiedKFold": StratifiedKFold,
          "GroupKFold": GroupKFold, "roc_auc_score": roc_auc_score}
    exec(src.replace("default_rng(0)", f"default_rng({seed})"), ns)
    X, y = tickets(np.random.default_rng(seed), 30)
    assert (X == ns["Xg"]).all() and (y == ns["yg"]).all()
    Xn, yn = tickets(np.random.default_rng(1000 + seed), 300)
    model = ns["forest"].fit(X, y)
    auc = roc_auc_score(yn, model.predict_proba(Xn)[:, 1])
    print(f"300 brand-new agents      AUC {auc:.3f}")
