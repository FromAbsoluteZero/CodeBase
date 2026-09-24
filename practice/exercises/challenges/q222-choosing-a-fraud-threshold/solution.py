import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def fraud_threshold(df, required_recall=0.80):
    """The figures described in README.md, as a dictionary."""
    X = df.drop(columns="Fraud")
    y = df["Fraud"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=7)
    model = make_pipeline(StandardScaler(), LogisticRegression(class_weight="balanced", max_iter=1000))
    model.fit(X_train, y_train)
    prob = model.predict_proba(X_test)[:, 1]

    def at(t):
        pred = (prob >= t).astype(int)
        return precision_score(y_test, pred, zero_division=0), recall_score(y_test, pred)

    # precision_recall_curve evaluates every distinct probability as a threshold; thresholds
    # rise and recall falls along the arrays, so the last index meeting the target is the highest.
    precision, recall, thresholds = precision_recall_curve(y_test, prob)
    ok = np.flatnonzero(recall[:-1] >= required_recall)
    chosen = thresholds[ok[-1]]
    p_def, r_def = at(0.5)
    p_thr, r_thr = at(chosen)
    return {
        "base_rate": float(y.mean()),
        "precision_at_default": float(p_def), "recall_at_default": float(r_def),
        "threshold": float(chosen),
        "precision_at_threshold": float(p_thr), "recall_at_threshold": float(r_thr),
    }
