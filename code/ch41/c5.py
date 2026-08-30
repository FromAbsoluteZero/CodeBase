# An agent must also decide WHEN to stop: continuing after the real
# answer is found wastes cost, and stopping too early returns an
# incomplete result. A confidence threshold controls this tradeoff
# directly, and the right setting depends on how those two costs compare.
def simulate_stopping(threshold, true_step_needed, max_steps, n_trials, seed):
    r = np.random.default_rng(seed)
    premature, wasted_steps, correct_stops = 0, 0, 0
    for _ in range(n_trials):
        stopped_at = None
        for step in range(1, max_steps + 1):
            # confidence rises noisily as the agent approaches the true answer
            true_progress = min(step / true_step_needed, 1.0)
            confidence = np.clip(true_progress + r.normal(0, 0.12), 0, 1)
            if confidence >= threshold:
                stopped_at = step
                break
        if stopped_at is None:
            stopped_at = max_steps
        if stopped_at < true_step_needed:
            premature += 1
        else:
            wasted_steps += (stopped_at - true_step_needed)
            correct_stops += 1
    return premature / n_trials, wasted_steps / n_trials

print(f"{'threshold':>11}{'premature-stop rate':>21}{'avg wasted steps':>18}")
for threshold in (0.5, 0.7, 0.85, 0.95, 0.99):
    premature, wasted = simulate_stopping(threshold, true_step_needed=8, max_steps=20,
                                          n_trials=10000, seed=41)
    print(f"{threshold:>11.2f}{premature:>21.4f}{wasted:>18.3f}")

print(f"\na low threshold stops early, often before the task is actually done;")
print(f"a high threshold rarely stops early, at the cost of extra steps")
print(f"spent confirming what was already true.")
