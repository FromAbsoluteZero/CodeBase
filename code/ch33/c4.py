# Train an RNN reading each digit row by row, and compare honestly
# against Chapter 30's fully connected network and Chapter 32's CNN,
# all on the identical images.
r4 = np.random.default_rng(33)
D_in, D_hid, D_out = 8, 16, 10
Wx = r4.normal(0, np.sqrt(1/D_in), (D_in, D_hid))
Wh = r4.normal(0, np.sqrt(1/D_hid), (D_hid, D_hid))
bh = np.zeros(D_hid)
Wo = r4.normal(0, np.sqrt(1/D_hid), (D_hid, D_out))
bo = np.zeros(D_out)

Ytr = np.eye(10)[ytr]
eta = 0.5

print(f"{'epoch':>7}{'train loss':>13}{'test accuracy':>15}")
for epoch in range(151):
    hs = rnn_forward(Xtr_img, Wx, Wh, bh)
    h_last = hs[:, -1]
    p = softmax(h_last @ Wo + bo)
    loss = -np.sum(Ytr * np.log(p + 1e-12)) / len(Xtr_img)

    dscore = (p - Ytr) / len(Xtr_img)
    dWo = h_last.T @ dscore
    dbo = dscore.sum(0)
    dh_last = dscore @ Wo.T
    dWx, dWh, dbh = rnn_backward(dh_last, Xtr_img, hs, Wx, Wh)

    Wo -= eta * dWo; bo -= eta * dbo
    Wx -= eta * dWx; Wh -= eta * dWh; bh -= eta * dbh

    if epoch % 30 == 0:
        hs_te = rnn_forward(Xte_img, Wx, Wh, bh)
        pred = softmax(hs_te[:, -1] @ Wo + bo).argmax(1)
        acc = (pred == yte).mean()
        print(f"{epoch:>7}{loss:>13.4f}{acc:>15.4f}")

hs_te = rnn_forward(Xte_img, Wx, Wh, bh)
rnn_pred = softmax(hs_te[:, -1] @ Wo + bo).argmax(1)
rnn_acc = (rnn_pred == yte).mean()
print(f"\nfinal RNN test accuracy: {rnn_acc:.4f}")

baseline = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
baseline.fit(Xtr, ytr)
print(f"fully connected baseline (Chapter 30 style): {baseline.score(Xte, yte):.4f}")
