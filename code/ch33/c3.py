# Backpropagation through time: the chain rule applied along the time
# axis, exactly as Chapter 32 applied it along space. Each step's
# gradient must account for two paths forward: into the output at that
# step, and into the next hidden state.
def rnn_forward(imgs, Wx, Wh, bh):
    n, T, D_in = imgs.shape
    D_hid = Wh.shape[0]
    hs = np.zeros((n, T + 1, D_hid))
    for t in range(T):
        hs[:, t+1] = np.tanh(imgs[:, t] @ Wx + hs[:, t] @ Wh + bh)
    return hs

def rnn_backward(dh_last, imgs, hs, Wx, Wh):
    n, T, D_in = imgs.shape
    D_hid = Wh.shape[0]
    dWx = np.zeros_like(Wx); dWh = np.zeros_like(Wh); dbh = np.zeros(D_hid)
    dh_next = dh_last.copy()
    for t in reversed(range(T)):
        dtanh = dh_next * (1 - hs[:, t+1]**2)
        dWx += imgs[:, t].T @ dtanh
        dWh += hs[:, t].T @ dtanh
        dbh += dtanh.sum(0)
        dh_next = dtanh @ Wh.T
    return dWx, dWh, dbh

r3 = np.random.default_rng(33)
D_in, D_hid = 8, 16
Wx = r3.normal(0, np.sqrt(1/D_in), (D_in, D_hid))
Wh = r3.normal(0, np.sqrt(1/D_hid), (D_hid, D_hid))
bh = np.zeros(D_hid)

imgs = Xtr_img[:4]
hs = rnn_forward(imgs, Wx, Wh, bh)
dh_last = r3.normal(size=(4, D_hid))               # a stand-in upstream gradient
dWx, dWh, dbh = rnn_backward(dh_last, imgs, hs, Wx, Wh)

def loss_fn(Wx_, Wh_, bh_):
    hs_ = rnn_forward(imgs, Wx_, Wh_, bh_)
    return np.sum(hs_[:, -1] * dh_last)

eps = 1e-5
print(f"{'target':>14}{'analytic':>12}{'numerical':>12}{'match':>8}")
for (i, j) in [(4, 8), (3, 4)]:
    orig = Wx[i, j]
    Wx[i, j] = orig + eps; lp = loss_fn(Wx, Wh, bh)
    Wx[i, j] = orig - eps; lm = loss_fn(Wx, Wh, bh)
    Wx[i, j] = orig
    numeric = (lp - lm) / (2 * eps)
    print(f"Wx{(i,j)}{dWx[i,j]:>12.6f}{numeric:>12.6f}{str(abs(numeric-dWx[i,j])<1e-4):>8}")
for (i, j) in [(12, 8), (4, 8)]:
    orig = Wh[i, j]
    Wh[i, j] = orig + eps; lp = loss_fn(Wx, Wh, bh)
    Wh[i, j] = orig - eps; lm = loss_fn(Wx, Wh, bh)
    Wh[i, j] = orig
    numeric = (lp - lm) / (2 * eps)
    print(f"Wh{(i,j)}{dWh[i,j]:>12.6f}{numeric:>12.6f}{str(abs(numeric-dWh[i,j])<1e-4):>8}")
