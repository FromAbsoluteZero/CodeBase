# Chain the router into a multi-step task: each step must pick the
# right tool AND that tool must succeed at its sub-task. A routing
# mistake is not usually recoverable mid-chain, since the wrong tool's
# output feeds directly into the next step.
def simulate_agent_task(n_steps, confusion, tool_success_given_correct, n_trials, seed):
    r = np.random.default_rng(seed)
    successes = 0
    for _ in range(n_trials):
        ok = True
        for step in range(n_steps):
            words, true_tool = tasks[step % len(tasks)]
            picked = route(words, confusion, r)
            if picked != true_tool:
                ok = False
                break
            if r.random() >= tool_success_given_correct:
                ok = False
                break
        successes += ok
    return successes / n_trials

print(f"{'steps':>7}{'confusion=0.0':>15}{'confusion=0.15':>16}{'confusion=0.30':>16}")
for n_steps in (1, 3, 5, 10):
    row = [n_steps]
    for confusion in (0.0, 0.15, 0.30):
        rate = simulate_agent_task(n_steps, confusion, tool_success_given_correct=0.95,
                                   n_trials=8000, seed=41)
        row.append(rate)
    print(f"{row[0]:>7}{row[1]:>15.4f}{row[2]:>16.4f}{row[3]:>16.4f}")

print(f"\neven a well-behaved 95%-reliable tool cannot rescue a chain that")
print(f"keeps routing to the wrong tool in the first place.")
