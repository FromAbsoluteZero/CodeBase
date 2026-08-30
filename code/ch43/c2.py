# The Population Stability Index bins both distributions the same way
# and compares bin proportions directly, which is what most production
# monitoring dashboards actually report rather than a raw p-value.
def psi(baseline, live, n_bins=10):
    edges = np.quantile(baseline, np.linspace(0, 1, n_bins + 1))
    edges[0], edges[-1] = -np.inf, np.inf
    base_counts, _ = np.histogram(baseline, bins=edges)
    live_counts, _ = np.histogram(live, bins=edges)
    base_pct = np.clip(base_counts / len(baseline), 1e-4, None)
    live_pct = np.clip(live_counts / len(live), 1e-4, None)
    return np.sum((live_pct - base_pct) * np.log(live_pct / base_pct))

print(f"{'week':>6}{'true mean shift':>17}{'PSI':>10}{'interpretation':>18}")
for week in range(0, 13):
    shift = week * 0.6
    live = r.normal(50 + shift, 10, 300)
    score = psi(baseline, live)
    if score < 0.1:
        label = "stable"
    elif score < 0.25:
        label = "moderate shift"
    else:
        label = "major shift"
    print(f"{week:>6}{shift:>17.1f}{score:>10.4f}{label:>18}")

print(f"\nPSI thresholds of 0.1 and 0.25 are the conventional industry cutoffs.")
