# When there is no single correct answer, human judgment becomes the
# reference, and human judgment has its own reliability to measure.
# Simulate raters against a KNOWN true quality, so agreement can be
# checked against ground truth rather than only against each other.
r = np.random.default_rng(40)
n_items = 300
true_quality = r.uniform(1, 5, n_items)              # a hidden "true" score, 1-5

def simulate_rater(true_scores, noise_sd, seed):
    rr = np.random.default_rng(seed)
    noisy = true_scores + rr.normal(0, noise_sd, len(true_scores))
    return np.clip(np.round(noisy), 1, 5).astype(int)

def cohen_kappa(a, b, n_categories=5):
    po = np.mean(a == b)
    pe = sum(np.mean(a == k) * np.mean(b == k) for k in range(1, n_categories + 1))
    return (po - pe) / (1 - pe)

print(f"{'rater noise (sd)':>18}{'raw agreement':>16}{'cohen kappa':>14}")
for noise in (0.2, 0.6, 1.0, 1.5, 2.5):
    agrees, kappas = [], []
    for pair_seed in range(20):                       # average over 20 independent rater pairs
        rater_a = simulate_rater(true_quality, noise, seed=1000 + pair_seed)
        rater_b = simulate_rater(true_quality, noise, seed=2000 + pair_seed)
        agrees.append(np.mean(rater_a == rater_b))
        kappas.append(cohen_kappa(rater_a, rater_b))
    print(f"{noise:>18.1f}{np.mean(agrees):>16.4f}{np.mean(kappas):>14.4f}")
