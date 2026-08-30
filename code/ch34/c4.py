# Multi-head attention runs several smaller attention operations in
# parallel, each with its own Q, K, V projections, then concatenates
# the results. Each head can specialize in a different kind of
# relationship between positions.
def multi_head_attention(X, Wq, Wk, Wv, Wo, n_heads):
    T, D = X.shape
    d_h = D // n_heads
    Q, K, V = X @ Wq, X @ Wk, X @ Wv                    # (T, D) each
    Qh = Q.reshape(T, n_heads, d_h).transpose(1, 0, 2)   # (heads, T, d_h)
    Kh = K.reshape(T, n_heads, d_h).transpose(1, 0, 2)
    Vh = V.reshape(T, n_heads, d_h).transpose(1, 0, 2)
    scores = Qh @ Kh.transpose(0, 2, 1) / np.sqrt(d_h)   # (heads, T, T)
    weights = softmax(scores)
    out_h = weights @ Vh                                 # (heads, T, d_h)
    concat = out_h.transpose(1, 0, 2).reshape(T, D)      # back to (T, D)
    return concat @ Wo, weights

r4 = np.random.default_rng(34)
T, D, n_heads = 5, 8, 2
X = r4.normal(size=(T, D))
Wq, Wk, Wv, Wo = (r4.normal(0, np.sqrt(1/D), (D, D)) for _ in range(4))

out, weights = multi_head_attention(X, Wq, Wk, Wv, Wo, n_heads)
print(f"input            {X.shape}")
print(f"per-head Q/K/V   ({n_heads}, {T}, {D // n_heads})")
print(f"attention weights {weights.shape}   one {T}x{T} matrix per head")
print(f"output           {out.shape}   back to the original width")

print(f"\nhead 0 attention weights for position 2: {weights[0, 2].round(3)}")
print(f"head 1 attention weights for position 2: {weights[1, 2].round(3)}")
print(f"the two heads attend differently, from the same input.")
