"""Serve the persisted churn pipeline behind a real HTTP endpoint.
Run c6.py first (it writes churn_pipeline.joblib), then:
    python serve.py
and, from another terminal:
    curl -s -X POST http://127.0.0.1:5043/predict \
        -H 'Content-Type: application/json' \
        -d '{"AnnualIncome": 52000, "Sessions": 12, "AvgBasket": 41.2,
             "Plan": "pro", "Channel": "web", "TenureDays": 400,
             "SignupMonth": 6, "BasketPerIncome": 0.79,
             "SessionsPerMonth": 0.87}'
"""
import pandas as pd
import joblib
from flask import Flask, request, jsonify

pipe = joblib.load("churn_pipeline.joblib")
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    row = pd.DataFrame([request.get_json()])
    proba = float(pipe.predict_proba(row)[0, 1])
    return jsonify({"churn_probability": round(proba, 4),
                    "will_churn": proba >= 0.5})

if __name__ == "__main__":
    app.run(port=5043)
