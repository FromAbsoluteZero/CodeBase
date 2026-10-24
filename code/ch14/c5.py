from sklearn.metrics import roc_auc_score, average_precision_score

auc = roc_auc_score(yte, p)
print(f"AUC: {auc:.4f}")
print(f"average precision: {average_precision_score(yte, p):.4f}")
print(f"a random model would score: 0.5000 AUC, "
      f"{yte.mean():.4f} average precision")

# check the interpretation directly
rng2 = np.random.default_rng(0)
leavers = p[yte == 1]
stayers = p[yte == 0]
wins = sum(rng2.choice(leavers) > rng2.choice(stayers)
           for _ in range(20000))
print(f"\nrandom leaver scored above random stayer: "
      f"{wins/20000:.4f} of the time")
