# A minimal CNN trained on the real data: four learned filters, max
# pooling, a fully connected output layer. The forward and backward
# passes are the vectorized, verified equivalent of Step 1's loop and
# Step 4's derivation, applied to a whole batch at once.
from numpy.lib.stride_tricks import sliding_window_view

def conv_forward(imgs, filters):
    windows = sliding_window_view(imgs, (3, 3), axis=(1, 2))
    return np.einsum('nijhw,fhw->nfij', windows, filters), windows

def conv_backward(dout, windows, filters):
    dfilters = np.einsum('nfij,nijhw->fhw', dout, windows)
    flipped = filters[:, ::-1, ::-1]
    pad = filters.shape[1] - 1
    dout_p = np.pad(dout, ((0, 0), (0, 0), (pad, pad), (pad, pad)))
    dwindows = sliding_window_view(dout_p, (3, 3), axis=(2, 3))
    dimgs = np.einsum('nfijhw,fhw->nij', dwindows, flipped)
    return dimgs, dfilters

def pool_forward(feats, size=2):
    n, nf, h, w = feats.shape
    r = feats.reshape(n, nf, h // size, size, w // size, size)
    out = r.max(axis=(3, 5))
    mask = (r == out[:, :, :, None, :, None])
    return out, mask

def pool_backward(dout, mask, size=2):
    n, nf, oh, ow = dout.shape
    d = dout[:, :, :, None, :, None] * mask
    return d.reshape(n, nf, oh * size, ow * size)

r = np.random.default_rng(32)
n_filters = 4
filters = r.normal(0, np.sqrt(2 / 9), (n_filters, 3, 3))
D_flat = n_filters * 3 * 3
Wf = r.normal(0, np.sqrt(2 / D_flat), (D_flat, 10))
bf = np.zeros(10)
Ytr = np.eye(10)[ytr]
eta = 0.3

print(f"{'epoch':>7}{'train loss':>13}{'test accuracy':>15}")
for epoch in range(151):
    conv_out, windows = conv_forward(Xtr_img, filters)
    relu_out = np.maximum(0, conv_out)
    pool_out, mask = pool_forward(relu_out)
    flat = pool_out.reshape(len(Xtr_img), -1)
    p = softmax(flat @ Wf + bf)
    loss = -np.sum(Ytr * np.log(p + 1e-12)) / len(Xtr_img)

    dscore = (p - Ytr) / len(Xtr_img)
    dWf = flat.T @ dscore
    dbf = dscore.sum(0)
    dflat = dscore @ Wf.T
    dpool = dflat.reshape(pool_out.shape)
    drelu = pool_backward(dpool, mask)
    dconv = drelu * (conv_out > 0)
    _, dfilters = conv_backward(dconv, windows, filters)

    Wf -= eta * dWf; bf -= eta * dbf
    filters -= eta * dfilters

    if epoch % 30 == 0:
        c_te, _ = conv_forward(Xte_img, filters)
        p_te, m_te = pool_forward(np.maximum(0, c_te))
        flat_te = p_te.reshape(len(Xte_img), -1)
        pred = softmax(flat_te @ Wf + bf).argmax(1)
        acc = (pred == yte).mean()
        print(f"{epoch:>7}{loss:>13.4f}{acc:>15.4f}")

c_te, _ = conv_forward(Xte_img, filters)
p_te, _ = pool_forward(np.maximum(0, c_te))
final_pred = softmax(p_te.reshape(len(Xte_img), -1) @ Wf + bf).argmax(1)
cnn_acc = (final_pred == yte).mean()
print(f"\nfinal CNN test accuracy: {cnn_acc:.4f}")
