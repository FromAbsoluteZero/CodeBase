# A convolution slides a small filter across an image, computing a dot
# product -- Chapter 9's dot product again -- at every position.
def convolve2d(img, kernel):
    kh, kw = kernel.shape
    h, w = img.shape
    out = np.zeros((h - kh + 1, w - kw + 1))
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            patch = img[i:i+kh, j:j+kw]
            out[i, j] = np.sum(patch * kernel)          # the dot product
    return out

vertical_edge = np.array([[1, 0, -1],
                          [1, 0, -1],
                          [1, 0, -1]], dtype=float)

img = X_img[0]                          # the first training digit, 8x8
feat = convolve2d(img, vertical_edge)

print(f"input image      {img.shape}")
print(f"3x3 filter        {vertical_edge.shape}")
print(f"output feature map {feat.shape}   <- shrinks by kernel_size - 1")
print(f"\none output value, by hand, at position (2, 2):")
patch = img[2:5, 2:5]
print(f"  image patch:\n{patch.round(2)}")
print(f"  patch . filter (elementwise, summed) = {np.sum(patch * vertical_edge):.4f}")
print(f"  convolve2d agrees: {feat[2, 2]:.4f}")
