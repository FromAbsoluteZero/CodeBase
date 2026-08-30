# The same vanishing-gradient problem from Chapter 31, on a new axis:
# instead of shrinking through many LAYERS, the gradient here shrinks
# through many TIME STEPS, because the same weight matrix multiplies
# the signal at every step, exactly like Chapter 31's Wh at every layer.
def tanh_grad(h):
    return 1 - h**2

r2 = np.random.default_rng(33)
D_hid = 16
Wh_decay = r2.normal(0, 0.3, (D_hid, D_hid))    # deliberately small-scale recurrent weights

def run_and_track_grad(n_steps, Wh_):
    h = np.zeros(D_hid)
    hs = [h]
    x = r2.normal(size=(n_steps, D_hid))
    for t in range(n_steps):
        h = np.tanh(x[t] + h @ Wh_)
        hs.append(h)
    # gradient of the LAST hidden state w.r.t. the FIRST: product of
    # tanh'(h_t) * Wh at every step in between
    grad = np.eye(D_hid)
    for t in range(1, n_steps + 1):
        grad = grad @ (np.diag(tanh_grad(hs[t])) @ Wh_)
    return np.linalg.norm(grad)

print(f"{'sequence length':>16}{'gradient norm, step 1 to last':>30}")
for n in (5, 10, 20, 40, 80):
    g = run_and_track_grad(n, Wh_decay)
    print(f"{n:>16}{g:>30.2e}")
