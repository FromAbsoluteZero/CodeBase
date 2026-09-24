import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def _features(df):
    signup_age = (pd.Timestamp("2024-12-31") - pd.to_datetime(df["SignupDate"])).dt.days
    return pd.DataFrame({"AnnualIncome": df["AnnualIncome"], "Sessions": df["Sessions"],
                         "AvgBasket": df["AvgBasket"], "SignupAge": signup_age})

def leakage_comparison(df):
    """honest_auc, leaky_auc and gap, as described in README.md."""
    X, y = _features(df), df["Churn"]
    folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
    honest = make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), LogisticRegression(max_iter=1000))
    honest_auc = cross_val_score(honest, X, y, cv=folds, scoring="roc_auc").mean()
    leaked = make_pipeline(SimpleImputer(strategy="median"), StandardScaler()).fit_transform(X)
    leaky_auc = cross_val_score(LogisticRegression(max_iter=1000), leaked, y, cv=folds, scoring="roc_auc").mean()
    return {"honest_auc": float(honest_auc), "leaky_auc": float(leaky_auc), "gap": float(leaky_auc - honest_auc)}
