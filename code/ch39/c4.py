# Does the same pattern hold on a real task, not just a constructed one?
# Reuse Chapter 35's exact source/target digit split: a CNN pretrained
# on digits zero through four, adapted to digits five through nine.
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from numpy.lib.stride_tricks import sliding_window_view

digits = load_digits()
X_img = digits.images / 16.0
y_all = digits.target
src_mask, tgt_mask = y_all < 5, y_all >= 5
Xsrc, ysrc = X_img[src_mask], y_all[src_mask]
Xtgt, ytgt = X_img[tgt_mask], y_all[tgt_mask] - 5
Xsrc_tr, Xsrc_te, ysrc_tr, ysrc_te = train_test_split(Xsrc, ysrc,
                                                      test_size=0.2,
                                                      stratify=ysrc,
                                                      random_state=0)
Xtgt_tr, Xtgt_te, ytgt_tr, ytgt_te = train_test_split(Xtgt, ytgt,
                                                      test_size=0.3,
                                                      stratify=ytgt,
                                                      random_state=0)

def conv_forward(imgs, filters):
    windows = sliding_window_view(imgs, (3, 3), axis=(1, 2))
    return np.einsum('nijhw,fhw->nfij', windows, filters), windows

def pool_forward(feats, size=2):
    n, nf, h, w = feats.shape
    rr = feats.reshape(n, nf, h // size, size, w // size, size)
    out = rr.max(axis=(3, 5))
    mask = (rr == out[:, :, :, None, :, None])
    return out, mask

def pool_backward(dout, mask, size=2):
    n, nf, oh, ow = dout.shape
    d = dout[:, :, :, None, :, None] * mask
    return d.reshape(n, nf, oh * size, ow * size)

def extract_features(imgs, filters):
    c, _ = conv_forward(imgs, filters)
    out, _ = pool_forward(np.maximum(0, c))
    return out.reshape(len(imgs), -1)

# pretrain filters on the source task (identical recipe to Chapter 35)
def train_cnn_source(Xtr, ytr, seed, n_filters=4, epochs=150):
    rr = np.random.default_rng(seed)
    filters = rr.normal(0, np.sqrt(2/9), (n_filters, 3, 3))
    D_flat = n_filters * 9
    Wf = rr.normal(0, np.sqrt(2/D_flat), (D_flat, 5)); bf = np.zeros(5)
    Y = np.eye(5)[ytr]
    for _ in range(epochs):
        c, windows = conv_forward(Xtr, filters)
        relu = np.maximum(0, c)
        pool, mask = pool_forward(relu)
        flat = pool.reshape(len(Xtr), -1)
        p = softmax(flat @ Wf + bf)
        dscore = (p - Y) / len(Xtr)
        dpool = (dscore @ Wf.T).reshape(pool.shape)
        dconv = pool_backward(dpool, mask) * (c > 0)
        dfilters = np.einsum('nfij,nijhw->fhw', dconv, windows)
        Wf -= 0.3 * (flat.T @ dscore); bf -= 0.3 * dscore.sum(0)
        filters -= 0.3 * dfilters
    return filters

src_filters = train_cnn_source(Xsrc_tr, ysrc_tr, seed=39)
D_feat = src_filters.size // 9 * 9         # 36, the pooled-feature dimension
feat_tr = extract_features(Xtgt_tr, src_filters)
feat_te = extract_features(Xtgt_te, src_filters)

def train_head_full(feat_tr, ytr, feat_te, yte, seed, epochs=200, eta=0.5):
    rr = np.random.default_rng(seed)
    D_ = feat_tr.shape[1]
    W = rr.normal(0, np.sqrt(1/D_), (D_, 5)); b = np.zeros(5)
    Y = np.eye(5)[ytr]
    for _ in range(epochs):
        p = softmax(feat_tr @ W + b)
        dscore = (p - Y) / len(feat_tr)
        W -= eta * (feat_tr.T @ dscore); b -= eta * dscore.sum(0)
    return (softmax(feat_te @ W + b).argmax(1) == yte).mean(), W.size

def train_head_lora(feat_tr, ytr, feat_te, yte, seed, rank,
                    epochs=400, eta=0.1):
    rr = np.random.default_rng(seed)
    D_ = feat_tr.shape[1]
    # frozen "pretrained" head init
    W0 = rr.normal(0, np.sqrt(1/D_), (D_, 5))
    A = rr.normal(0, 0.01, (D_, rank)); B = np.zeros((rank, 5))
    b = np.zeros(5)
    Y = np.eye(5)[ytr]
    for _ in range(epochs):
        W = W0 + A @ B
        p = softmax(feat_tr @ W + b)
        dscore = (p - Y) / len(feat_tr)
        dW = feat_tr.T @ dscore
        dA = dW @ B.T; dB = A.T @ dW          # both from the SAME A and B
        A -= eta * dA; B -= eta * dB; b -= eta * dscore.sum(0)
    W = W0 + A @ B
    acc = (softmax(feat_te @ W + b).argmax(1) == yte).mean()
    return acc, A.size + B.size

acc_full, params_full = train_head_full(feat_tr, ytgt_tr, feat_te,
                                        ytgt_te, seed=39)
print(f"real digit task, full fine-tune of the head: {acc_full:.4f}  "
      f"({params_full} params)")
for rank in (1, 2, 4, 8):
    acc_lora, params_lora = train_head_lora(feat_tr, ytgt_tr, feat_te,
                                            ytgt_te, seed=39, rank=rank)
    print(f"real digit task, LoRA rank {rank}:            {acc_lora:.4f}  "
          f"({params_lora} params, "
          f"{100*params_lora/params_full:.0f}% of full)")
