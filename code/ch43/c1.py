# Data drift: the distribution of an input feature shifts after
# deployment. The Kolmogorov-Smirnov test, from Chapter 8's hypothesis
# testing toolkit, compares a recent window of live data against the
# distribution the model was trained on.
r = np.random.default_rng(43)
baseline = r.normal(50, 10, 2000)          # the feature's distribution at training time

def ks_test(baseline, live):
    stat, p = stats.ks_2samp(baseline, live)
    return stat, p

print(f"{'week':>6}{'true mean shift':>17}{'KS statistic':>14}{'p-value':>12}{'flagged?':>10}")
for week in range(0, 13):
    shift = week * 0.6                       # the feature drifts gradually, 0.6 units per week
    live = r.normal(50 + shift, 10, 300)      # this week's monitoring window
    stat, p = ks_test(baseline, live)
    flagged = "yes" if p < 0.01 else "no"
    print(f"{week:>6}{shift:>17.1f}{stat:>14.4f}{p:>12.4f}{flagged:>10}")
