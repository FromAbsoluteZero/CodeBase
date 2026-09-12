# 600 tickets triaged by four agents. Each agent has their own habit: some
# escalate far more than others. A model given anything that identifies the
# agent can predict the agent's habit instead of doing the task.
rng = np.random.default_rng(0)
n, agent = 600, None
agent = rng.integers(0, 4, n)                    # the repeated entity
habit = np.array([0.10, 0.40, 0.60, 0.90])[agent]  # base escalation rate
signal = rng.normal(0, 1, n)                     # the real, weak evidence

Xg = np.c_[signal * 0.6,                          # weak genuine signal
           agent, habit + rng.normal(0, .02, n)]  # agent fingerprint
yg = (rng.random(n) < np.clip(habit + 0.10 * signal, 0, 1)).astype(int)

m = LogisticRegression(max_iter=1000)
rand = cross_val_score(m, Xg, yg, scoring="roc_auc",
                       cv=StratifiedKFold(4, shuffle=True,
                                          random_state=0)).mean()
grp = cross_val_score(m, Xg, yg, groups=agent, scoring="roc_auc",
                      cv=GroupKFold(4)).mean()
print(f"random 4-fold   AUC {rand:.4f}   (agents appear on both sides)")
print(f"grouped 4-fold  AUC {grp:.4f}   (each agent held out entirely)")
print(f"the random split flatters the model by {rand - grp:+.4f}")
