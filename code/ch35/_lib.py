import numpy as np, warnings; warnings.filterwarnings("ignore")
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from numpy.lib.stride_tricks import sliding_window_view

digits = load_digits()
X_all = digits.images / 16.0
y_all = digits.target

# Source task: digits 0-4. Target task: digits 5-9, a disjoint set of
# classes the source network never saw during pretraining.
src_mask = y_all < 5
tgt_mask = y_all >= 5

Xsrc, ysrc = X_all[src_mask], y_all[src_mask]
Xtgt, ytgt = X_all[tgt_mask], y_all[tgt_mask] - 5     # relabel to 0-4

Xsrc_tr, Xsrc_te, ysrc_tr, ysrc_te = train_test_split(
    Xsrc, ysrc, test_size=0.2, stratify=ysrc, random_state=0)
Xtgt_tr, Xtgt_te, ytgt_tr, ytgt_te = train_test_split(
    Xtgt, ytgt, test_size=0.3, stratify=ytgt, random_state=0)

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

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
