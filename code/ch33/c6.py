# Attention removes the bottleneck by letting the output look at EVERY
# hidden state, not just the last, weighted by how relevant each one is.
# A learned query vector scores every timestep; softmax turns the
# scores into weights; the output uses their weighted sum.
def train_recall_attention(seq_len, seed, epochs=120, D_hid=12):
    Xs, ys = make_recall_task(600, seq_len, seed)
    Xs_te, ys_te = make_recall_task(200, seq_len, seed + 1)
    rr = np.random.default_rng(seed)
    D_in, D_out = 3, 3
    Wx = rr.normal(0, np.sqrt(1/D_in), (D_in, D_hid))
    Wh = rr.normal(0, np.sqrt(1/D_hid), (D_hid, D_hid))
    bh = np.zeros(D_hid)
    q = rr.normal(0, np.sqrt(1/D_hid), D_hid)             # the learned query
    Wo = rr.normal(0, np.sqrt(1/D_hid), (D_hid, D_out))
    bo = np.zeros(D_out)
    Y = np.eye(3)[ys]
    eta = 0.5
    for _ in range(epochs):
        hs = rnn_forward(Xs, Wx, Wh, bh)[:, 1:]     # drop the t=0 zero state
        scores = hs @ q                             # (n, T)
        weights = softmax(scores)                   # attention weights
        # weighted sum of states
        context = np.einsum('nt,nth->nh', weights, hs)
        p = softmax(context @ Wo + bo)
        dscore = (p - Y) / len(Xs)
        dWo = context.T @ dscore; dbo = dscore.sum(0)
        dcontext = dscore @ Wo.T
        dweights = np.einsum('nh,nth->nt', dcontext, hs)
        dscores = weights * (dweights - (dweights * weights).sum(1,
                             keepdims=True))
        dhs = np.einsum('nt,nh->nth', weights,
                        dcontext) + np.einsum('nt,h->nth', dscores, q)
        dq = np.einsum('nth,nt->h', hs, dscores)
        # Attention gives every step its own gradient, so all of
        # dhs enters the walk back, not only the last step's.
        # Feeding only dhs[:, -1] to Step 3's routine would
        # discard the rest and leave the recurrent weights
        # on the same single long path this step removes.
        hs_full = np.concatenate(
            [np.zeros((len(Xs), 1, D_hid)), hs], axis=1)
        dWx = np.zeros_like(Wx); dWh = np.zeros_like(Wh)
        dbh = np.zeros(D_hid); dh_next = np.zeros((len(Xs), D_hid))
        for t in reversed(range(seq_len)):
            dh = dh_next + dhs[:, t]
            dtanh = dh * (1 - hs_full[:, t+1]**2)
            dWx += Xs[:, t].T @ dtanh
            dWh += hs_full[:, t].T @ dtanh
            dbh += dtanh.sum(0)
            dh_next = dtanh @ Wh.T
        Wo -= eta*dWo; bo -= eta*dbo; q -= eta*dq
        Wx -= eta*dWx; Wh -= eta*dWh; bh -= eta*dbh
    hs_te = rnn_forward(Xs_te, Wx, Wh, bh)[:, 1:]
    w_te = softmax(hs_te @ q)
    ctx_te = np.einsum('nt,nth->nh', w_te, hs_te)
    acc = (softmax(ctx_te @ Wo + bo).argmax(1) == ys_te).mean()
    return acc, w_te

print(f"{'sequence length':>16}{'plain RNN':>12}{'with attention':>16}")
for L in (2, 5, 10, 20, 40):
    acc_attn, w = train_recall_attention(L, seed=33)
    acc_plain = plain_recall[L]           # the value Step 5 just computed
    print(f"{L:>16}{acc_plain:>12.4f}{acc_attn:>16.4f}")

print(f"\nattention weights on the length-40 task, averaged "
      f"over the test set:")
print(w.mean(0).round(3))
