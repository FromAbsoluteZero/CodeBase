# Retrying a failed step raises the effective per-step success rate, at
# a real cost: each retry is another full call to the model. Both the
# benefit and the cost need to be counted together.
def simulate_with_retries(n_steps, p_per_step, max_retries, n_trials, seed):
    r = np.random.default_rng(seed)
    total_calls = 0
    successes = 0
    for _ in range(n_trials):
        calls_this_trial = 0
        task_ok = True
        for _ in range(n_steps):
            attempt, ok = 0, False
            while attempt <= max_retries:
                calls_this_trial += 1
                attempt += 1
                if r.random() < p_per_step:
                    ok = True
                    break
            if not ok:
                task_ok = False
                break
        total_calls += calls_this_trial
        successes += task_ok
    return successes / n_trials, total_calls / n_trials

print(f"{'max retries':>12}{'task success rate':>19}{'avg calls per task':>20}")
for max_retries in (0, 1, 2, 3):
    rate, calls = simulate_with_retries(n_steps=10, p_per_step=0.90, max_retries=max_retries,
                                        n_trials=20000, seed=41)
    print(f"{max_retries:>12}{rate:>19.4f}{calls:>20.2f}")

print(f"\nat zero retries, average cost is BELOW ten calls, 6.54, because")
print(f"a task that fails partway through stops immediately rather than")
print(f"finishing all ten steps: failure is cheap here, precisely because")
print(f"nothing catches it. Each retry buys real accuracy at a real,")
print(f"compounding cost.")
