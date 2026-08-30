# Backpropagation is the chain rule from Chapter 10, applied layer by
# layer. Each gradient below is checked against Chapter 10's numerical
# method before it is trusted.
Y = np.eye(10)[y[:5]]                 # one-hot targets, 5 examples
Xb = X[:5]

def loss_and_grads(Xb, Y):
    z1, a1, z2, p = forward(Xb)
    n = len(Xb)
    loss = -np.sum(Y * np.log(p + 1e-12)) / n

    dz2 = (p - Y) / n                              # softmax + cross-entropy
    dW2 = a1.T @ dz2
    db2 = dz2.sum(0)
    da1 = dz2 @ W2.T
    dz1 = da1 * (z1 > 0)                            # ReLU gradient
    dW1 = Xb.T @ dz1
    db1 = dz1.sum(0)
    return loss, (dW1, db1, dW2, db2)

loss, (dW1, db1, dW2, db2) = loss_and_grads(Xb, Y)

# numerical check on a handful of W1 entries, exactly Chapter 10's method
eps = 1e-5
checks = [(43, 7), (27, 21), (43, 16)]
print(f"{'entry':>10}{'analytic':>12}{'numerical':>12}{'match':>8}")
for i, j in checks:
    orig = W1[i, j]
    W1[i, j] = orig + eps
    lp, _ = loss_and_grads(Xb, Y)
    W1[i, j] = orig - eps
    lm, _ = loss_and_grads(Xb, Y)
    W1[i, j] = orig
    numeric = (lp - lm) / (2 * eps)
    match = abs(numeric - dW1[i, j]) < 1e-4
    print(f"({i:>2},{j:>2}){dW1[i,j]:>12.6f}{numeric:>12.6f}{str(match):>8}")

print(f"\nstarting loss on these five examples: {loss:.4f}")
print(f"(a fresh, untrained network on a 10-class problem should sit")
print(f" near ln(10) = {np.log(10):.4f})")
