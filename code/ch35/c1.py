# Pretrain a small CNN to distinguish digits zero through four. The
# filters it learns are Chapter 32's exact architecture, trained on a
# task that has never seen a five, six, seven, eight, or nine.
def train_cnn(Xtr, ytr, Xte, yte, n_classes, seed, epochs=150, n_filters=4):
    r = np.random.default_rng(seed)
    filters = r.normal(0, np.sqrt(2 / 9), (n_filters, 3, 3))
    D_flat = n_filters * 3 * 3
    Wf = r.normal(0, np.sqrt(2 / D_flat), (D_flat, n_classes))
    bf = np.zeros(n_classes)
    Y = np.eye(n_classes)[ytr]
    eta = 0.3
    for epoch in range(epochs):
        conv_out, windows = conv_forward(Xtr, filters)
        relu_out = np.maximum(0, conv_out)
        pool_out, mask = pool_forward(relu_out)
        flat = pool_out.reshape(len(Xtr), -1)
        p = softmax(flat @ Wf + bf)
        dscore = (p - Y) / len(Xtr)
        dWf = flat.T @ dscore
        dbf = dscore.sum(0)
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
    acc = (pred == yte).mean()
    return filters, Wf, bf, acc

src_filters, src_Wf, src_bf, src_acc = train_cnn(
    Xsrc_tr, ysrc_tr, Xsrc_te, ysrc_te, n_classes=5, seed=35)
print(f"source task (digits 0-4) test accuracy: {src_acc:.4f}")
print(f"learned filters shape: {src_filters.shape}")
print(f"\nthese four filters have seen only zeros, ones, twos, threes,")
print(f"and fours. They have never seen a five, six, seven, eight, or nine.")
