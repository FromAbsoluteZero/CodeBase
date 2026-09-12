import numpy as np, warnings; warnings.filterwarnings("ignore")
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

digits = load_digits()
X, y = digits.data / 16.0, digits.target
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2,
                                      stratify=y, random_state=0)
