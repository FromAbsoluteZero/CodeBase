names = ["Acme Cafe", "Bean Bros", "Office Depot", "Corner Kiosk"]
# spend across Beans, Merch, Equipment
X = np.array([
    [820.0,  60.0,  40.0],
    [760.0,  90.0,  30.0],
    [ 40.0, 120.0, 900.0],
    [110.0, 480.0, 130.0],
])

norms = np.linalg.norm(X, axis=1, keepdims=True)
Xn = X / norms                 # each row now has length 1
S = Xn @ Xn.T                  # every pairwise cosine at once

print("total spend:", [f"${v:,.0f}" for v in X.sum(axis=1)])
print()
print(f"Acme vs Bean Bros:    {S[0,1]:.3f}")
print(f"Acme vs Office Depot: {S[0,2]:.3f}")
print(f"Acme vs Corner Kiosk: {S[0,3]:.3f}")
