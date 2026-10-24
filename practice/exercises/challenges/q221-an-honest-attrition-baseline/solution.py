import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def attrition_baseline(df):
    """majority_accuracy, model_accuracy and model_auc on a stratified 80/20 test split."""
    X = df.drop(columns="Attrition")
    y = df["Attrition"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    categorical = ["Department", "OverTime"]
    numeric = [c for c in X.columns if c not in categorical]
    prep = ColumnTransformer([("cat", OneHotEncoder(), categorical), ("num", StandardScaler(), numeric)])
    model = Pipeline([("prep", prep), ("clf", LogisticRegression(max_iter=1000))])
    model.fit(X_train, y_train)
    majority = y_train.mode()[0]
    return {
        "majority_accuracy": float((y_test == majority).mean()),
        "model_accuracy": float(accuracy_score(y_test, model.predict(X_test))),
        "model_auc": float(roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])),
    }
