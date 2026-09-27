import numpy as np
import pandas as pd

def baseline_maes(df, horizon=90):
    """MAE of the mean, naive and seasonal-naive baselines on the last `horizon` days, and the best."""
    series = df.sort_values("Date")["Revenue"].to_numpy()
    train, test = series[:-horizon], series[-horizon:]
    mean_forecast = np.full(horizon, train.mean())
    naive_forecast = np.full(horizon, train[-1])
    last_week = train[-7:]
    seasonal_forecast = np.array([last_week[i % 7] for i in range(horizon)])
    maes = {
        "mean": float(np.abs(test - mean_forecast).mean()),
        "naive": float(np.abs(test - naive_forecast).mean()),
        "seasonal_naive": float(np.abs(test - seasonal_forecast).mean()),
    }
    maes["best"] = min(maes, key=maes.get)
    return maes
