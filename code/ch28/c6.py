from sklearn.ensemble import RandomForestRegressor

f = pd.DataFrame({"y": s})
f["dow"], f["month"] = f.index.dayofweek, f.index.month
f["lag_7"]   = f["y"].shift(7)            # same weekday, one week back
f["lag_14"]  = f["y"].shift(14)
f["roll_28"] = f["y"].shift(7).rolling(28).mean()
f = f.dropna()

X = ["dow", "month", "lag_7", "lag_14", "roll_28"]
tr, te = f[:-H], f[-H:]
m = RandomForestRegressor(n_estimators=300,
                          random_state=0).fit(tr[X], tr["y"])

err = np.abs(te["y"] - m.predict(te[X]))
print(f"  random forest      MAE {err.mean():>7,.0f}")
for n, v in sorted(zip(X, m.feature_importances_), key=lambda p: -p[1]):
    print(f"  {n:<10} {v:.3f}")
