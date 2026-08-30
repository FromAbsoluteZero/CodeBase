from statsmodels.tsa.holtwinters import ExponentialSmoothing

fit = ExponentialSmoothing(train, trend="add",
                           seasonal="add", seasonal_periods=7).fit()
hw = fit.forecast(H)

sn = train.iloc[-7:].values.tolist() * 4
print(f"  seasonal naive     MAE {mae(sn):>7,.0f}")
print(f"  Holt-Winters       MAE {mae(hw):>7,.0f}")
for k in ("smoothing_level", "smoothing_trend", "smoothing_seasonal"):
    print(f"  {k:<20} {fit.params[k]:.3f}")
