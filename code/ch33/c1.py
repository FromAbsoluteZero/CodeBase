# A recurrent network reads a sequence one step at a time, carrying a
# hidden state forward. The same weights are reused at every step: this
# is parameter sharing across time, exactly as Chapter 32 shared a
# filter's weights across space.
r = np.random.default_rng(33)
D_in, D_hid = 8, 16                      # 8 pixels per row, 16-unit hidden state
Wx = r.normal(0, np.sqrt(1/D_in), (D_in, D_hid))
Wh = r.normal(0, np.sqrt(1/D_hid), (D_hid, D_hid))
bh = np.zeros(D_hid)

def rnn_step(x_t, h_prev):
    return np.tanh(x_t @ Wx + h_prev @ Wh + bh)

img = Xtr_img[0]                         # one digit, 8 rows
h = np.zeros(D_hid)                      # hidden state starts at zero

print(f"{'timestep':>9}{'row (input)':>14}{'|hidden state|':>16}")
for t in range(8):
    h = rnn_step(img[t], h)
    print(f"{t:>9}{str(img[t].shape):>14}{np.linalg.norm(h):>16.4f}")

print(f"\nafter all 8 rows, one hidden state of size {D_hid} summarizes")
print(f"the entire image: {h.round(3)}")
