import numpy as np, pandas as pd, warnings; warnings.filterwarnings("ignore")
from scipy.stats import loguniform, randint
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import (GridSearchCV, RandomizedSearchCV,
    cross_val_score, StratifiedKFold, train_test_split)
from sklearn.datasets import make_classification
df = pd.read_csv("customers.csv", parse_dates=["SignupDate"])
y = df.pop("Churn").values
df = df.drop(columns=["City", "SignupDate"])
NUM = ["AnnualIncome", "Sessions", "AvgBasket"]
CAT = ["Plan", "Channel"]
def base_pipe(clf):
    num = Pipeline([("imp", SimpleImputer(strategy="median")),
                    ("sc", StandardScaler())])
    return Pipeline([("pre", ColumnTransformer([
                        ("n", num, NUM),
                        ("c", OneHotEncoder(handle_unknown="ignore"), CAT)])),
                     ("clf", clf)])
cv = StratifiedKFold(5, shuffle=True, random_state=0)
