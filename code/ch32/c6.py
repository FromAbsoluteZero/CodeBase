# Raw accuracy is not the only axis that matters. Shift every test image
# by one pixel and see which architecture degrades less: this is what
# the parameter-sharing argument actually predicts.
def cnn_predict(imgs):
    c, _ = conv_forward(imgs, filters)
    p, _ = pool_forward(np.maximum(0, c))
    return softmax(p.reshape(len(imgs), -1) @ Wf + bf).argmax(1)

Xte_shifted = np.roll(Xte_img, 1, axis=2)             # every test image, shifted right

cnn_acc_orig = (cnn_predict(Xte_img) == yte).mean()
cnn_acc_shift = (cnn_predict(Xte_shifted) == yte).mean()

fc_baseline = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
fc_baseline.fit(Xtr, ytr)
fc_acc_orig = fc_baseline.score(Xte, yte)
fc_acc_shift = fc_baseline.score(Xte_shifted.reshape(len(Xte), -1), yte)

print(f"{'model':<28}{'original':>10}{'shifted':>10}{'drop':>9}")
print(f"{'fully connected (logreg)':<28}{fc_acc_orig:>10.4f}{fc_acc_shift:>10.4f}"
      f"{fc_acc_orig-fc_acc_shift:>9.4f}")
print(f"{'CNN, 4 filters':<28}{cnn_acc_orig:>10.4f}{cnn_acc_shift:>10.4f}"
      f"{cnn_acc_orig-cnn_acc_shift:>9.4f}")
