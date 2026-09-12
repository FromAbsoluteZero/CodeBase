# Train on the real data: forward, backward, update, repeat.
def forward_train(Xb, W1, b1, W2, b2):
    z1 = Xb @ W1 + b1
    a1 = np.maximum(0, z1)
    z2 = a1 @ W2 + b2
    return z1, a1, softmax(z2)

D_in, H, D_out = 64, 32, 10
r5 = np.random.default_rng(30)
W1t = r5.normal(0, np.sqrt(2/D_in), (D_in, H)); b1t = np.zeros(H)
W2t = r5.normal(0, np.sqrt(2/H), (H, D_out));    b2t = np.zeros(D_out)
Ytr = np.eye(10)[ytr]
eta = 0.5

print(f"{'epoch':>7}{'train loss':>13}{'test accuracy':>15}")
for epoch in range(401):
    z1, a1, p = forward_train(Xtr, W1t, b1t, W2t, b2t)
    loss = -np.sum(Ytr * np.log(p + 1e-12)) / len(Xtr)

    dz2 = (p - Ytr) / len(Xtr)
    dW2, db2 = a1.T @ dz2, dz2.sum(0)
    dz1 = (dz2 @ W2t.T) * (z1 > 0)
    dW1, db1 = Xtr.T @ dz1, dz1.sum(0)
    W1t -= eta * dW1; b1t -= eta * db1
    W2t -= eta * dW2; b2t -= eta * db2

    if epoch % 100 == 0:
        _, _, pte = forward_train(Xte, W1t, b1t, W2t, b2t)
        acc = (pte.argmax(1) == yte).mean()
        print(f"{epoch:>7}{loss:>13.4f}{acc:>15.4f}")

_, _, pte = forward_train(Xte, W1t, b1t, W2t, b2t)
final_acc = (pte.argmax(1) == yte).mean()
print(f"\nfinal test accuracy: {final_acc:.4f}")
