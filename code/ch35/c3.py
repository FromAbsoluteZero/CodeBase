# Transfer learning is expected to earn its keep when target data is
# scarce. Vary how much target training data is available and compare
# frozen transfer against training a small CNN from scratch on that
# same, limited data, at every scale from extreme few-shot upward.
def train_cnn_head_only(feat_tr, ytr, n_classes, seed, epochs=200):
    r = np.random.default_rng(seed)
    D = feat_tr.shape[1]
    W = r.normal(0, np.sqrt(1 / D), (D, n_classes))
    b = np.zeros(n_classes)
    Y = np.eye(n_classes)[ytr]
    eta = 0.5
    for _ in range(epochs):
        p = softmax(feat_tr @ W + b)
        dscore = (p - Y) / len(feat_tr)
        W -= eta * (feat_tr.T @ dscore)
        b -= eta * dscore.sum(0)
    return W, b

print(f"{'target examples':>17}{'transfer (frozen)':>19}{'from scratch':>14}")
rng_sub = np.random.default_rng(35)
for n_per_class in (2, 3, 5, 15, 40, 100):
    idx = []
    for c in range(5):
        class_idx = np.where(ytgt_tr == c)[0]
        idx.extend(rng_sub.choice(class_idx, size=min(n_per_class, len(class_idx)),
                                  replace=False))
    idx = np.array(idx)
    Xsub, ysub = Xtgt_tr[idx], ytgt_tr[idx]

    feat_sub = extract_features(Xsub, src_filters)
    feat_te = extract_features(Xtgt_te, src_filters)
    W, b = train_cnn_head_only(feat_sub, ysub, n_classes=5, seed=35)
    acc_transfer = (softmax(feat_te @ W + b).argmax(1) == ytgt_te).mean()

    _, _, _, acc_scratch = train_cnn(Xsub, ysub, Xtgt_te, ytgt_te,
                                     n_classes=5, seed=35, epochs=150)

    print(f"{len(idx):>17}{acc_transfer:>19.4f}{acc_scratch:>14.4f}")
