# A synthetic lending scenario, built so the true qualification rate
# genuinely differs between two groups -- exactly the condition under
# which fairness definitions are known to conflict. Group membership
# itself is not a model input; only correlated features are, and each
# individual's features are drawn conditional on their OWN true
# repayment outcome, so the model has genuine signal to learn from.
r = np.random.default_rng(44)
n = 4000
group = r.integers(0, 2, n)
base_rate = np.where(group == 0, 0.75, 0.55)    # true qualification rate per group
will_repay = r.random(n) < base_rate
y = will_repay.astype(int)

# features genuinely separate repayers from defaulters, with a
# group-level offset layered on top, reflecting real disparities in
# income and credit history that correlate with, but do not equal,
# group membership
income = r.normal(45 + 20 * y + 8 * (group == 0), 10, n)
credit_history = r.normal(50 + 25 * y + 5 * (group == 0), 12, n)

X = np.column_stack([income, credit_history])
model = LogisticRegression().fit(X, y)
p_repay = model.predict_proba(X)[:, 1]
pred = (p_repay >= 0.5).astype(int)

print(f"n = {n}, group 0: {np.sum(group==0)}, group 1: {np.sum(group==1)}")
print(f"true qualification rate, group 0: {y[group==0].mean():.4f}")
print(f"true qualification rate, group 1: {y[group==1].mean():.4f}")
print(f"overall model accuracy: {(pred == y).mean():.4f}")
print(f"\napproval rate (model), group 0: {pred[group==0].mean():.4f}")
print(f"approval rate (model), group 1: {pred[group==1].mean():.4f}")
print(f"demographic parity gap: {abs(pred[group==0].mean() - pred[group==1].mean()):.4f}")
