import numpy as np, pandas as pd, warnings; warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (roc_auc_score, average_precision_score,
    precision_recall_curve, roc_curve, confusion_matrix, brier_score_loss)
from sklearn.calibration import CalibratedClassifierCV, calibration_curve
tx = pd.read_csv("transactions.csv")
X = tx.drop(columns="Fraud").values
y = tx["Fraud"].values
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.35,
                                      random_state=0, stratify=y)
