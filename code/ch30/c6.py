# The baseline discipline from Chapter 1: before trusting the network,
# check what a much simpler model achieves on the same split.
baseline = make_pipeline(StandardScaler(),
                         LogisticRegression(max_iter=2000))
baseline.fit(Xtr, ytr)
base_acc = baseline.score(Xte, yte)

print(f"logistic regression baseline:  {base_acc:.4f}")
print(f"hand-built network:            {final_acc:.4f}")
print(f"gain over the baseline:        {final_acc - base_acc:+.4f}")

# where does the network still fail?
_, _, pte = forward_train(Xte, W1t, b1t, W2t, b2t)
pred = pte.argmax(1)
wrong = np.where(pred != yte)[0]
print(f"\n{len(wrong)} of {len(yte)} test digits misclassified")
print(f"{'true':>6}{'predicted':>11}{'confidence':>13}")
for i in wrong[:6]:
    print(f"{yte[i]:>6}{pred[i]:>11}{pte[i, pred[i]]:>13.3f}")

# Step 2's rings, given to the same network: 8 ReLU units, 2 classes,
# trained on 300 points and scored on 100 points it never saw.
Xr, Xs, yr, ys = train_test_split(Xc, yc, test_size=0.25,
                                  stratify=yc, random_state=0)
r6 = np.random.default_rng(30)
V1 = r6.normal(0, 1, (2, 8));            u1 = np.zeros(8)
V2 = r6.normal(0, np.sqrt(2/8), (8, 2)); u2 = np.zeros(2)
Yr = np.eye(2)[yr]
for epoch in range(2000):
    z1, a1, p = forward_train(Xr, V1, u1, V2, u2)
    dz2 = (p - Yr) / len(Xr)
    dz1 = (dz2 @ V2.T) * (z1 > 0)
    V2 -= eta * (a1.T @ dz2); u2 -= eta * dz2.sum(0)
    V1 -= eta * (Xr.T @ dz1); u1 -= eta * dz1.sum(0)

lin_r = LogisticRegression().fit(Xr, yr)
_, _, pr = forward_train(Xr, V1, u1, V2, u2)
_, _, ps = forward_train(Xs, V1, u1, V2, u2)
print(f"\nrings: {len(Xr)} training points, {len(Xs)} test points")
print(f"{'':>14}{'train':>8}{'test':>8}")
print(f"{'linear model':>14}{lin_r.score(Xr, yr):>8.3f}"
      f"{lin_r.score(Xs, ys):>8.3f}")
print(f"{'ReLU network':>14}{(pr.argmax(1) == yr).mean():>8.3f}"
      f"{(ps.argmax(1) == ys).mean():>8.3f}")
