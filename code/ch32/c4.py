# The backward pass through a convolution, derived and then checked
# exactly as Chapter 10 prescribed. This is the last hand-derived
# gradient in this book, and it is noticeably more work than any before
# it -- which is itself the argument for what comes after this chapter.
def conv_backward(dout, img, kernel):
    kh, kw = kernel.shape
    dkernel = np.zeros_like(kernel)
    for di in range(kh):
        for dj in range(kw):
            dkernel[di, dj] = np.sum(
                dout * img[di:di+dout.shape[0], dj:dj+dout.shape[1]])

    flipped = kernel[::-1, ::-1]
    pad_h, pad_w = kh - 1, kw - 1
    dout_padded = np.pad(dout, ((pad_h, pad_h), (pad_w, pad_w)))
    dimg = convolve2d(dout_padded, flipped)
    return dimg, dkernel

img = X_img[3]
kernel = vertical_edge.copy()
feat = convolve2d(img, kernel)
dout = np.random.default_rng(32).normal(size=feat.shape)   # a stand-in upstream gradient

dimg, dkernel = conv_backward(dout, img, kernel)
print(f"dkernel shape {dkernel.shape}   dimg shape {dimg.shape}")

# numerical check, Chapter 10's method, on three kernel entries and
# three image pixels
eps = 1e-5
def loss(img_, kernel_):
    return np.sum(convolve2d(img_, kernel_) * dout)

print(f"\n{'target':>14}{'analytic':>12}{'numerical':>12}{'match':>8}")
for (di, dj) in [(0, 0), (1, 1), (2, 2)]:
    orig = kernel[di, dj]
    kernel[di, dj] = orig + eps; lp = loss(img, kernel)
    kernel[di, dj] = orig - eps; lm = loss(img, kernel)
    kernel[di, dj] = orig
    numeric = (lp - lm) / (2 * eps)
    match = abs(numeric - dkernel[di, dj]) < 1e-4
    print(f"kernel{(di,dj)}{dkernel[di,dj]:>12.6f}{numeric:>12.6f}{str(match):>8}")

for (pi, pj) in [(1, 1), (4, 4), (6, 6)]:
    orig = img[pi, pj]
    img[pi, pj] = orig + eps; lp = loss(img, kernel)
    img[pi, pj] = orig - eps; lm = loss(img, kernel)
    img[pi, pj] = orig
    numeric = (lp - lm) / (2 * eps)
    match = abs(numeric - dimg[pi, pj]) < 1e-4
    print(f"pixel{(pi,pj)} {dimg[pi,pj]:>12.6f}{numeric:>12.6f}{str(match):>8}")
