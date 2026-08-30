import numpy as np, pandas as pd, warnings; warnings.filterwarnings("ignore")
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import (StandardScaler, OneHotEncoder,
                                   OrdinalEncoder, TargetEncoder)
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold, train_test_split
df = pd.read_csv("customers.csv", parse_dates=["SignupDate"])
y = df.pop("Churn").values
cv = StratifiedKFold(5, shuffle=True, random_state=0)
NUM = ["AnnualIncome", "Sessions", "AvgBasket"]
LOWCARD = ["Plan", "Channel"]
