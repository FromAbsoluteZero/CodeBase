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
