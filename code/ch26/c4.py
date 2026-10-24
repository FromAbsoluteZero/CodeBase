# DBSCAN has no k, but it has eps -- and it is far more sensitive to eps
# than k-means is to k.
real_noise = truth == "unclassifiable"
print(f"{'eps':>6}{'clusters':>10}{'noise':>8}{'ARI':>8}"
      f"{'noise precision':>17}")
for eps in (0.25, 0.30, 0.35, 0.40, 0.45, 0.55):
    db = DBSCAN(eps=eps, min_samples=12).fit(X)
    lab = db.labels_
    n = len(set(lab)) - (1 if -1 in lab else 0)
    flagged = lab == -1
    prec = (flagged & real_noise).sum() / max(flagged.sum(), 1)
    print(f"{eps:>6.2f}{n:>10}{int(flagged.sum()):>8}"
          f"{adjusted_rand_score(truth, lab):>8.3f}{prec:>17.1%}")
