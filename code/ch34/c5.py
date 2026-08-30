# The self-attention backward pass. Every position is simultaneously a
# query, a key, and a value for every other position, so a gradient
# arriving at the output must be routed back through all three roles.
# This is the last gradient this book derives, and it earns that title.
def attn_forward(X, Wq, Wk, Wv):
    Q, K, V = X @ Wq, X @ Wk, X @ Wv
    d_k = Q.shape[-1]
    scores = (Q @ K.T) / np.sqrt(d_k)
    weights = softmax(scores)
    out = weights @ V
    return out, (X, Q, K, V, weights, d_k)

def attn_backward(dout, cache, Wq, Wk, Wv):
    X, Q, K, V, weights, d_k = cache
    dV = weights.T @ dout
    dweights = dout @ V.T
    dscores = weights * (dweights - (dweights * weights).sum(-1, keepdims=True))
    dscores = dscores / np.sqrt(d_k)
    dQ = dscores @ K
    dK = dscores.T @ Q
    dWq = X.T @ dQ; dWk = X.T @ dK; dWv = X.T @ dV
    dX = dQ @ Wq.T + dK @ Wk.T + dV @ Wv.T
    return dX, dWq, dWk, dWv

r5 = np.random.default_rng(34)
T, D = 5, 8
X = r5.normal(size=(T, D))
Wq, Wk, Wv = (r5.normal(0, np.sqrt(1/D), (D, D)) for _ in range(3))

out, cache = attn_forward(X, Wq, Wk, Wv)
dout = r5.normal(size=out.shape)
dX, dWq, dWk, dWv = attn_backward(dout, cache, Wq, Wk, Wv)

def loss_fn(X_, Wq_, Wk_, Wv_):
    o, _ = attn_forward(X_, Wq_, Wk_, Wv_)
    return np.sum(o * dout)

eps = 1e-5
print(f"{'target':>12}{'analytic':>12}{'numerical':>12}{'match':>8}")
for name, arr, grad in [('Wq', Wq, dWq), ('Wk', Wk, dWk), ('Wv', Wv, dWv), ('X', X, dX)]:
    i, j = int(np.abs(grad).argmax() // grad.shape[1]), int(np.abs(grad).argmax() % grad.shape[1])
    orig = arr[i, j]
    arr[i, j] = orig + eps; lp = loss_fn(X, Wq, Wk, Wv)
    arr[i, j] = orig - eps; lm = loss_fn(X, Wq, Wk, Wv)
    arr[i, j] = orig
    numeric = (lp - lm) / (2 * eps)
    match = abs(numeric - grad[i, j]) < 1e-4
    print(f"{name+str((i,j)):>12}{grad[i,j]:>12.6f}{numeric:>12.6f}{str(match):>8}")
