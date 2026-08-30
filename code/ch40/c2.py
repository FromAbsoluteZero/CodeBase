# A rubric splits one holistic judgment into several specific criteria,
# then averages them. If each criterion's noise is at least partly
# independent of the others, averaging reduces the total noise, the
# same law of large numbers Chapter 17 relied on for cross-validation.
def simulate_holistic(true_scores, noise_sd, seed):
    rr = np.random.default_rng(seed)
    return true_scores + rr.normal(0, noise_sd, len(true_scores))

def simulate_rubric(true_scores, noise_sd, n_criteria, seed):
    rr = np.random.default_rng(seed)
    criteria_scores = np.stack([
        true_scores + rr.normal(0, noise_sd, len(true_scores))
        for _ in range(n_criteria)
    ])
    return criteria_scores.mean(axis=0)               # the rubric score: an average

print(f"{'method':<28}{'error vs true quality (RMSE)':>30}")
holistic = simulate_holistic(true_quality, noise_sd=1.0, seed=40)
rmse_holistic = np.sqrt(np.mean((holistic - true_quality) ** 2))
print(f"{'single holistic rating':<28}{rmse_holistic:>30.4f}")

for n_criteria in (2, 3, 5, 10):
    rubric = simulate_rubric(true_quality, noise_sd=1.0, n_criteria=n_criteria, seed=40)
    rmse_rubric = np.sqrt(np.mean((rubric - true_quality) ** 2))
    print(f"{'rubric, ' + str(n_criteria) + ' criteria':<28}{rmse_rubric:>30.4f}")

print(f"\neach criterion is exactly as noisy as the holistic rating alone;")
print(f"only averaging several of them, not any single criterion, reduces")
print(f"the error.")
