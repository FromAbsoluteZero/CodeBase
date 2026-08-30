# A minimal transformer block: self-attention, a residual connection,
# then a small feedforward layer, on Chapter 33's exact recall task
# (the class is planted at position 0, however long the sequence runs).
def make_recall_task(n_samples, seq_len, seed):
    rr = np.random.default_rng(seed)
    first = rr.integers(0, 3, n_samples)
    seq = rr.normal(0, 0.3, (n_samples, seq_len, 3))
    seq[np.arange(n_samples), 0] = np.eye(3)[first]
    return seq, first

def batch_self_attention(X, Wq, Wk, Wv):
    Q, K, V = X @ Wq, X @ Wk, X @ Wv                  # (n, T, D)
    d_k = Q.shape[-1]
    scores = np.einsum('ntd,nsd->nts', Q, K) / np.sqrt(d_k)
    weights = softmax(scores)
    out = np.einsum('nts,nsd->ntd', weights, V)
    return out, (X, Q, K, V, weights, d_k)

def train_transformer(seq_len, seed, epochs=150, D=16):
    Xs, ys = make_recall_task(600, seq_len, seed)
    Xs_te, ys_te = make_recall_task(200, seq_len, seed + 1)
    rr = np.random.default_rng(seed)
    D_in, D_out = 3, 3
    We = rr.normal(0, np.sqrt(1/D_in), (D_in, D))       # embed into D dims
    Wq, Wk, Wv = (rr.normal(0, np.sqrt(1/D), (D, D)) for _ in range(3))
    W1 = rr.normal(0, np.sqrt(2/D), (D, D)); b1 = np.zeros(D)     # tiny FFN
    Wo = rr.normal(0, np.sqrt(1/D), (D, D_out)); bo = np.zeros(D_out)
    Y = np.eye(3)[ys]
    eta = 0.3
    for _ in range(epochs):
        Xe = Xs @ We
        attn_out, cache = batch_self_attention(Xe, Wq, Wk, Wv)
        resid1 = Xe + attn_out
        ff = np.maximum(0, resid1 @ W1 + b1)
        resid2 = resid1 + ff
        pooled = resid2[:, -1]                          # last position's output
        p = softmax(pooled @ Wo + bo)

        dscore = (p - Y) / len(Xs)
        dWo = pooled.T @ dscore; dbo = dscore.sum(0)
        dpooled = dscore @ Wo.T
        dresid2 = np.zeros_like(resid2); dresid2[:, -1] = dpooled
        dff = dresid2 * (ff > 0)
        dW1 = resid1.reshape(-1, D).T @ dff.reshape(-1, D)
        db1 = dff.reshape(-1, D).sum(0)
        dresid1 = dresid2 + dff @ W1.T
        dattn = dresid1
        X_, Q, K, V, weights, d_k = cache
        dV = np.einsum('nts,ntd->nsd', weights, dattn)
        dweights = np.einsum('ntd,nsd->nts', dattn, V)
        dscores = weights * (dweights - (dweights * weights).sum(-1, keepdims=True))
        dscores = dscores / np.sqrt(d_k)
        dQ = np.einsum('nts,nsd->ntd', dscores, K)
        dK = np.einsum('nts,ntd->nsd', dscores, Q)
        dWq = np.einsum('ntd,nte->de', X_, dQ)
        dWk = np.einsum('ntd,nte->de', X_, dK)
        dWv = np.einsum('ntd,nte->de', X_, dV)
        dXe = dresid1 + dQ @ Wq.T + dK @ Wk.T + dV @ Wv.T
        dWe = np.einsum('ntd,nte->de', Xs, dXe)

        Wo -= eta*dWo; bo -= eta*dbo; W1 -= eta*dW1; b1 -= eta*db1
        Wq -= eta*dWq; Wk -= eta*dWk; Wv -= eta*dWv; We -= eta*dWe

    Xe_te = Xs_te @ We
    attn_te, cache_te = batch_self_attention(Xe_te, Wq, Wk, Wv)
    weights_te = cache_te[4]
    last_pos_weights = weights_te[:, -1, :].mean(0)       # avg attention FROM the last position
    r1_te = Xe_te + attn_te
    ff_te = np.maximum(0, r1_te @ W1 + b1)
    r2_te = r1_te + ff_te
    pred = softmax(r2_te[:, -1] @ Wo + bo).argmax(1)
    acc = (pred == ys_te).mean()
    return acc, last_pos_weights

print(f"{'length':>8}{'RNN+attn':>10}{'transformer':>13}{'weight on pos 0':>18}"
      f"{'chance (1/T)':>14}")
prior_attn = {2: 1.0, 5: 1.0, 10: 0.99, 20: 0.995, 40: 0.99}
for L in (2, 5, 10, 20, 40):
    acc, w = train_transformer(L, seed=34)
    print(f"{L:>8}{prior_attn[L]:>10.4f}{acc:>13.4f}{w[0]:>18.4f}{1/L:>14.4f}")
