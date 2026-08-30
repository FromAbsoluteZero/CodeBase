# Fine-tuning starts from the transferred filters rather than random
# ones, then keeps training everything, filters included, on the
# target task. It should combine a good starting point with the
# ability to specialize.
def fine_tune(Xtr, ytr, Xte, yte, init_filters, n_classes, seed, epochs=150):
    r = np.random.default_rng(seed)
    filters = init_filters.copy()                    # start from transfer, not random
    D_flat = filters.shape[0] * 3 * 3
    Wf = r.normal(0, np.sqrt(2 / D_flat), (D_flat, n_classes))
    bf = np.zeros(n_classes)
    Y = np.eye(n_classes)[ytr]
    eta = 0.3
    for _ in range(epochs):
        conv_out, windows = conv_forward(Xtr, filters)
        relu_out = np.maximum(0, conv_out)
        pool_out, mask = pool_forward(relu_out)
        flat = pool_out.reshape(len(Xtr), -1)
        p = softmax(flat @ Wf + bf)
        dscore = (p - Y) / len(Xtr)
        dWf = flat.T @ dscore; dbf = dscore.sum(0)
        dflat = dscore @ Wf.T
        dpool = dflat.reshape(pool_out.shape)
        drelu = pool_backward(dpool, mask)
        dconv = drelu * (conv_out > 0)
        _, dfilters = conv_backward(dconv, windows, filters)
        Wf -= eta * dWf; bf -= eta * dbf
        filters -= eta * dfilters
    c_te, _ = conv_forward(Xte, filters)
    p_te, _ = pool_forward(np.maximum(0, c_te))
    pred = softmax(p_te.reshape(len(Xte), -1) @ Wf + bf).argmax(1)
    return (pred == yte).mean()

print(f"{'target examples':>17}{'frozen transfer':>18}{'from scratch':>14}{'fine-tuned':>12}")
rng_sub2 = np.random.default_rng(35)
for n_per_class in (2, 5, 15, 40):
    idx = []
    for c in range(5):
        class_idx = np.where(ytgt_tr == c)[0]
        idx.extend(rng_sub2.choice(class_idx, size=min(n_per_class, len(class_idx)),
                                   replace=False))
    idx = np.array(idx)
    Xsub, ysub = Xtgt_tr[idx], ytgt_tr[idx]

    feat_sub = extract_features(Xsub, src_filters)
    feat_te = extract_features(Xtgt_te, src_filters)
    W, b = train_cnn_head_only(feat_sub, ysub, n_classes=5, seed=35)
    acc_frozen = (softmax(feat_te @ W + b).argmax(1) == ytgt_te).mean()

    _, _, _, acc_scratch = train_cnn(Xsub, ysub, Xtgt_te, ytgt_te,
                                     n_classes=5, seed=35, epochs=150)

    acc_finetune = fine_tune(Xsub, ysub, Xtgt_te, ytgt_te, src_filters,
                             n_classes=5, seed=35)

    print(f"{len(idx):>17}{acc_frozen:>18.4f}{acc_scratch:>14.4f}{acc_finetune:>12.4f}")
