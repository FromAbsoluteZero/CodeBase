import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

for z in [-4, -1, 0, 1, 4]:
    print(f"  z = {z:>3}  ->  p = {sigmoid(z):.4f}")

# log loss punishes confident mistakes far more than squared error
print(f"\n{'predicted':>10}{'squared err':>14}{'log loss':>12}")
for p in [0.5, 0.1, 0.01]:
    sq = (1 - p) ** 2
    ll = -np.log(p)
    print(f"{p:>10.2f}{sq:>14.4f}{ll:>12.4f}")
print("\n(true answer is 1 in every row above)")
