# Without a nonlinearity, stacking layers is pointless: two linear layers
# collapse into one. The nonlinearity is what makes depth mean anything.
from sklearn.datasets import make_circles
Xc, yc = make_circles(n_samples=400, noise=0.08, factor=0.4, random_state=0)

# A "network" with no activation: z2 = (z1 @ W2) = ((x @ W1) @ W2) = x @ (W1 @ W2)
# which is just one big matrix -- a linear model wearing a costume.
r2 = np.random.default_rng(30)
W1c = r2.normal(size=(2, 8)); W2c = r2.normal(size=(8, 1))
combined = W1c @ W2c
print(f"W1 shape {W1c.shape}, W2 shape {W2c.shape}")
print(f"W1 @ W2 shape {combined.shape}  <- collapses to one 2x1 matrix")
print("two linear layers ARE one linear layer, just slower to compute.")

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
lin = LogisticRegression().fit(Xc, yc)
print(f"\nlinear model on a ring inside a ring: "
      f"{accuracy_score(yc, lin.predict(Xc)):.3f} accuracy")
print("no straight line separates a ring from its centre, so a stack of")
print("linear layers scores exactly what guessing scores. This is why")
print("ReLU exists: it lets each layer bend the boundary, not just")
print("rotate it.")
