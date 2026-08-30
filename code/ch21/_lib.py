import numpy as np, pandas as pd, warnings, time; warnings.filterwarnings("ignore")
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import cross_val_score, StratifiedKFold, train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.datasets import make_moons, make_circles
df = pd.read_csv("customers.csv", parse_dates=["SignupDate"])
y = df.pop("Churn").values
df = df.drop(columns=["City", "SignupDate"])
NUM = ["AnnualIncome", "Sessions", "AvgBasket"]
CAT = ["Plan", "Channel"]
def pipe(clf, scale=True):
    steps = [("imp", SimpleImputer(strategy="median"))]
    if scale:
        steps.append(("sc", StandardScaler()))
    return Pipeline([("pre", ColumnTransformer([
                        ("n", Pipeline(steps), NUM),
                        ("c", OneHotEncoder(handle_unknown="ignore"), CAT)])),
                     ("clf", clf)])
cv = StratifiedKFold(5, shuffle=True, random_state=0)
