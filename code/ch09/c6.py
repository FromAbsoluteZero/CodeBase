w = np.array([1.0, 50.0, 30.0])
cust["score"] = X @ w

top = cust.sort_values("score", ascending=False).head(5)
print(top.round(1).to_string())
