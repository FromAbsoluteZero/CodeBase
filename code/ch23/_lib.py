import numpy as np, pandas as pd, warnings; warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (roc_auc_score, average_precision_score,
                             precision_score, recall_score, confusion_matrix)
tx = pd.read_csv("transactions.csv")
X = tx.drop(columns="Fraud").values
y = tx["Fraud"].values
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.35,
                                      random_state=0, stratify=y)
C_FP, C_FN = 6.0, 204.0        # review cost; expected loss prevented
