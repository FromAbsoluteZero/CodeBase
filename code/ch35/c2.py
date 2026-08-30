# Freeze the source-trained filters and use them only to extract
# features from the target task's images. Train nothing but a new
# linear head. A random, untrained set of filters is the control: if
# frozen features help only because ANY fixed projection helps, the
# random filters should do just as well.
def extract_features(imgs, filters):
    c, _ = conv_forward(imgs, filters)
    p, _ = pool_forward(np.maximum(0, c))
    return p.reshape(len(imgs), -1)

def train_head(feat_tr, ytr, feat_te, yte, n_classes, seed, epochs=200):
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
    pred = softmax(feat_te @ W + b).argmax(1)
    return (pred == yte).mean()

feat_tr_transfer = extract_features(Xtgt_tr, src_filters)
feat_te_transfer = extract_features(Xtgt_te, src_filters)
acc_transfer = train_head(feat_tr_transfer, ytgt_tr, feat_te_transfer, ytgt_te,
                          n_classes=5, seed=35)

r_rand = np.random.default_rng(999)
random_filters = r_rand.normal(0, np.sqrt(2/9), src_filters.shape)
feat_tr_random = extract_features(Xtgt_tr, random_filters)
feat_te_random = extract_features(Xtgt_te, random_filters)
acc_random = train_head(feat_tr_random, ytgt_tr, feat_te_random, ytgt_te,
                        n_classes=5, seed=35)

print(f"target task (digits 5-9), linear head only, no filter training")
print(f"  frozen SOURCE-TRAINED filters: {acc_transfer:.4f}")
print(f"  frozen RANDOM filters:         {acc_random:.4f}")
print(f"\nsame architecture, same amount of training, only the filters differ.")
