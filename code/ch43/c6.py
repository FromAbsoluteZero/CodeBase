# Persisting and serving a model: every model this book has trained so
# far was discarded the moment its script ended. A model that is
# actually used sits on disk between requests and answers them one at a
# time, behind an interface. This reuses Chapter 24's own
# engineered-features pipeline on customers.csv (Step 4 there) rather
# than inventing a new model.
import os as _os, shutil as _shutil, json, subprocess, sys, time
import joblib, pandas as pd, requests
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

if not _os.path.exists("customers.csv"):
    for _d in ("../../data/generated", "../data/generated",
              "data/generated"):
        if _os.path.exists(_os.path.join(_d, "customers.csv")):
            _shutil.copy(_os.path.join(_d, "customers.csv"),
                        "customers.csv")
            break

df = pd.read_csv("customers.csv", parse_dates=["SignupDate"])
y = df.pop("Churn").values
NUM = ["AnnualIncome", "Sessions", "AvgBasket"]
LOWCARD = ["Plan", "Channel"]

def add_features(d):
    d = d.copy()
    d["TenureDays"] = (pd.Timestamp("2025-01-01")
                       - d["SignupDate"]).dt.days
    d["SignupMonth"] = d["SignupDate"].dt.month
    d["BasketPerIncome"] = d["AvgBasket"] / (d["AnnualIncome"] / 1000)
    d["SessionsPerMonth"] = d["Sessions"] / (d["TenureDays"] / 30 + 1)
    return d.drop(columns=["SignupDate", "City"])

NUM2 = NUM + ["TenureDays", "SignupMonth", "BasketPerIncome",
             "SessionsPerMonth"]
d2 = add_features(df)
X_train, X_test, y_train, y_test = train_test_split(
    d2, y, test_size=0.2, stratify=y, random_state=0)
num = Pipeline([("imp", SimpleImputer(strategy="median")),
               ("sc", StandardScaler())])
pipe = Pipeline([
    ("pre", ColumnTransformer([
        ("n", num, NUM2),
        ("c", OneHotEncoder(handle_unknown="ignore"), LOWCARD)])),
    ("clf", LogisticRegression(max_iter=2000))])
pipe.fit(X_train, y_train)

# write the fitted pipeline to disk, then load a fresh copy back, as a
# server run in a separate process would
joblib.dump(pipe, "churn_pipeline.joblib")
reloaded = joblib.load("churn_pipeline.joblib")

sample = X_test.iloc[[0]]
original = pipe.predict_proba(sample)[0, 1]
from_disk = reloaded.predict_proba(sample)[0, 1]
print(f"prediction before saving: {original:.4f}   "
      f"after reload: {from_disk:.4f}")
print(f"identical: {original == from_disk}")

# serve.py, shipped alongside this file, loads that same file and
# answers POST requests. Start it exactly as a reader would in a
# second terminal, wait for it to come up, then send it one request.
if not _os.path.exists("serve.py"):
    for _d in ("../../code/ch43", "../code/ch43", "code/ch43"):
        if _os.path.exists(_os.path.join(_d, "serve.py")):
            _shutil.copy(_os.path.join(_d, "serve.py"), "serve.py")
            break
proc = subprocess.Popen([sys.executable, "serve.py"],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)
time.sleep(2)
payload = {
    "AnnualIncome": round(float(sample.AnnualIncome.iloc[0]), 2),
    "Sessions": int(sample.Sessions.iloc[0]),
    "AvgBasket": round(float(sample.AvgBasket.iloc[0]), 2),
    "Plan": sample.Plan.iloc[0],
    "Channel": sample.Channel.iloc[0],
    "TenureDays": int(sample.TenureDays.iloc[0]),
    "SignupMonth": int(sample.SignupMonth.iloc[0]),
    "BasketPerIncome": round(float(sample.BasketPerIncome.iloc[0]), 4),
    "SessionsPerMonth": round(float(sample.SessionsPerMonth.iloc[0]), 4),
}
reference = pipe.predict_proba(pd.DataFrame([payload]))[0, 1]
resp = requests.post("http://127.0.0.1:5043/predict", json=payload,
                     timeout=5)
proc.terminate()
proc.wait(timeout=5)

print(f"\n$ curl -s -X POST http://127.0.0.1:5043/predict \\")
print(f"    -H 'Content-Type: application/json' \\")
print(f"    -d '{json.dumps(payload, indent=2)}'")
print(json.dumps(resp.json()))

served = resp.json()["churn_probability"]
print(f"\nserved prediction matches the pipeline's own predict_proba "
      f"on the")
print(f"same input: {abs(served - reference) < 1e-4}  "
      f"({served} vs {reference:.4f})")
