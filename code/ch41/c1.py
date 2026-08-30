# An agent completes a task by taking several steps in sequence: plan,
# call a tool, read the result, decide the next step, repeat. If each
# step succeeds independently with probability p, the whole task
# succeeds only if every step does, and that compounds fast.
def simulate_task_success(n_steps, p_per_step, n_trials, seed):
    r = np.random.default_rng(seed)
    successes = r.random((n_trials, n_steps)) < p_per_step
    return successes.all(axis=1).mean()

print(f"{'steps':>7}{'p=0.99':>10}{'p=0.95':>10}{'p=0.90':>10}{'p=0.80':>10}")
for n_steps in (1, 3, 5, 10, 20, 40):
    row = [n_steps]
    for p in (0.99, 0.95, 0.90, 0.80):
        rate = simulate_task_success(n_steps, p, n_trials=20000, seed=41)
        row.append(rate)
    print(f"{row[0]:>7}{row[1]:>10.4f}{row[2]:>10.4f}{row[3]:>10.4f}{row[4]:>10.4f}")

print(f"\nexact formula: p^n_steps. at p=0.95, n=20: {0.95**20:.4f}")
