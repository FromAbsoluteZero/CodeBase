# The fix for concept drift is to monitor what the model actually gets
# right, not just what it sees. This requires labels to eventually
# arrive, often delayed, but even a small labelled sample each week is
# enough to catch what distribution monitoring cannot see at all.
# Reruns the identical scenario from Step 3, on the identical random
# draws, so the two diagnostics describe the same twelve weeks rather
# than two separately-sampled ones.
r3 = np.random.default_rng(430)
_ = r3.normal(50, 10, 2000)                # advance the stream past x_train, exactly as Step 3 did

print(f"{'week':>6}{'model accuracy':>16}{'flagged (acc < 0.85)?':>23}")
for week in range(0, 13):
    x_live = r3.normal(50, 10, 500)
    true_boundary_now = 50 + week * 2.5
    y_live = make_labels(x_live, true_boundary_now)
    pred = (x_live > model_boundary).astype(int)
    acc = (pred == y_live).mean()
    flagged = "yes -- retrain" if acc < 0.85 else "no"
    print(f"{week:>6}{acc:>16.4f}{flagged:>23}")

print(f"\na performance monitor catches the problem at week 2, when the true")
print(f"boundary has moved only 5 of its eventual 30 units, one sixth of the")
print(f"way there. The feature-distribution test in Step 3 never flags this")
print(f"drift at all across the same twelve weeks.")
