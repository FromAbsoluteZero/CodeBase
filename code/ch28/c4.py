import numpy as np

H = 28                                   # horizon: four weeks
train, test = s[:-H], s[-H:]
mae = lambda pred: np.mean(np.abs(test.values - np.asarray(pred)))

print(f"train ends {train.index.max().date()},  test is {len(test)} days")
for name, pred in [
        ("last value",       np.repeat(train.iloc[-1], H)),
        ("last 28-day mean", np.repeat(train.iloc[-28:].mean(), H)),
        ("seasonal naive",   train.iloc[-7:].values.tolist() * 4)]:
    print(f"  {name:<18} MAE {mae(pred):>7,.0f}")
