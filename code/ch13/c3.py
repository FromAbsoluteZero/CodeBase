fitted = X @ beta

print(f"1. residuals centered?   mean {resid.mean():.6f}")
print(f"2. residual sd          ${resid.std(ddof=1):,.2f}")
print(f"3. symmetric?           skew {pd.Series(resid).skew():.3f}")

# 4. constant spread? correlate |residual| with the prediction
hetero = np.corrcoef(np.abs(resid), fitted)[0, 1]
print(f"4. constant spread?     corr(|resid|, fitted) = {hetero:.4f}")

# make it concrete: spread within thirds of the predictions
band = pd.qcut(fitted, 3, labels=["low", "mid", "high"])
spread = pd.Series(resid).groupby(band, observed=True).std().round(1)
print("\nresidual sd within prediction thirds:")
print(spread.to_string())
