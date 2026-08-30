# Pooling shrinks the feature map and buys a little tolerance to small
# shifts: the same loudest signal survives even if it moves by a pixel.
def max_pool2d(feat, size=2):
    h, w = feat.shape
    oh, ow = h // size, w // size
    out = np.zeros((oh, ow))
    for i in range(oh):
        for j in range(ow):
            out[i, j] = feat[i*size:(i+1)*size, j*size:(j+1)*size].max()
    return out

feat = convolve2d(X_img[0], vertical_edge)
pooled = max_pool2d(feat, size=2)
print(f"feature map     {feat.shape}")
print(f"after 2x2 pool  {pooled.shape}")

# shift the image by one pixel and compare the pooled output
shifted = np.roll(X_img[0], 1, axis=1)
feat_shifted = convolve2d(shifted, vertical_edge)
pooled_shifted = max_pool2d(feat_shifted, size=2)

diff_raw = np.abs(feat[:5, :5] - feat_shifted[:5, :5]).mean()
diff_pooled = np.abs(pooled - pooled_shifted).mean()
print(f"\nafter shifting the image by one pixel:")
print(f"  mean change in the raw feature map: {diff_raw:.4f}")
print(f"  mean change after pooling:          {diff_pooled:.4f}")
