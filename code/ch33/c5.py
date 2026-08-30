# The bottleneck problem is distinct from vanishing gradients: even a
# perfectly trained RNN must compress an entire sequence into one
# fixed-size hidden state. Test this directly with a task whose answer
# depends only on the FIRST element, however long the sequence grows.
def make_recall_task(n_samples, seq_len, seed):
    rr = np.random.default_rng(seed)
    first = rr.integers(0, 3, n_samples)                 # the answer to recall
    seq = rr.normal(0, 0.3, (n_samples, seq_len, 3))
    seq[np.arange(n_samples), 0] = np.eye(3)[first]        # plant it at step 0
    return seq, first

def train_recall(seq_len, seed, epochs=120, D_hid=12):
    Xs, ys = make_recall_task(600, seq_len, seed)
    Xs_te, ys_te = make_recall_task(200, seq_len, seed + 1)
    rr = np.random.default_rng(seed)
    D_in, D_out = 3, 3
    Wx = rr.normal(0, np.sqrt(1/D_in), (D_in, D_hid))
    Wh = rr.normal(0, np.sqrt(1/D_hid), (D_hid, D_hid))
    bh = np.zeros(D_hid)
    Wo = rr.normal(0, np.sqrt(1/D_hid), (D_hid, D_out))
    bo = np.zeros(D_out)
    Y = np.eye(3)[ys]
    eta = 0.5
    for _ in range(epochs):
        hs = rnn_forward(Xs, Wx, Wh, bh)
        h_last = hs[:, -1]
        p = softmax(h_last @ Wo + bo)
        dscore = (p - Y) / len(Xs)
        dWo = h_last.T @ dscore; dbo = dscore.sum(0)
        dh_last = dscore @ Wo.T
        dWx, dWh, dbh = rnn_backward(dh_last, Xs, hs, Wx, Wh)
        Wo -= eta*dWo; bo -= eta*dbo; Wx -= eta*dWx; Wh -= eta*dWh; bh -= eta*dbh
    hs_te = rnn_forward(Xs_te, Wx, Wh, bh)
    acc = (softmax(hs_te[:, -1] @ Wo + bo).argmax(1) == ys_te).mean()
    return acc

print(f"{'sequence length':>16}{'recall accuracy':>18}")
for L in (2, 5, 10, 20, 40):
    acc = train_recall(L, seed=33)
    print(f"{L:>16}{acc:>18.4f}")
print(f"\nchance accuracy on three classes: 0.333")
