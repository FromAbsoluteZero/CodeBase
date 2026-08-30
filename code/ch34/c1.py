# Self-attention: every position produces a query, a key, and a value.
# The query asks a question; the key advertises what a position holds;
# the value is what gets returned if that position is selected. This is
# Chapter 9's dot product, used to decide what to look at.
r = np.random.default_rng(34)
T, D = 5, 8                              # 5 positions, 8-dim embeddings
X = r.normal(size=(T, D))

Wq = r.normal(0, np.sqrt(1/D), (D, D))
Wk = r.normal(0, np.sqrt(1/D), (D, D))
Wv = r.normal(0, np.sqrt(1/D), (D, D))

Q = X @ Wq
K = X @ Wk
V = X @ Wv
print(f"X (input)   {X.shape}")
print(f"Q, K, V     {Q.shape}   one query, key, and value PER POSITION")

scores = Q @ K.T                          # every position scores every other
print(f"\nQ @ K.T     {scores.shape}   position i's query dotted with every key")
print(f"scores[2]   {scores[2].round(2)}   <- how position 2 scores all 5 positions")

weights = softmax(scores)
out = weights @ V
print(f"\nattention weights for position 2: {weights[2].round(3)}   sums to {weights[2].sum():.4f}")
print(f"output for position 2 = weighted sum of all 5 value vectors: {out[2, :4].round(3)}...")
