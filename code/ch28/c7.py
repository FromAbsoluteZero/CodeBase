def fold(cut):
    tr, te = s[:cut], s[cut:cut + H]
    rep = np.array(tr.iloc[-7:].values.tolist() * 4)
    sn = np.mean(np.abs(te.values - rep))
    hw = ExponentialSmoothing(tr, trend="add", seasonal="add",
                              seasonal_periods=7).fit().forecast(H)
    return {"seasonal naive": sn,
            "Holt-Winters": np.mean(np.abs(te.values - hw.values)),
            "fold ends": s.index[cut + H - 1].date()}

cuts = [len(s) - H * k for k in range(6, 0, -1)]
t = pd.DataFrame([fold(c) for c in cuts]).set_index("fold ends")
print(t.round(0).to_string())
print("\nmean across six folds")
print(t.mean().round(0).to_string())
