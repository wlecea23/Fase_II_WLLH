import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(
        os.path.abspath(__file__)
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model.pkl"
)

SCALER_PATH = os.path.join(
    BASE_DIR,
    "scaler.pkl"
)

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


def predict(data):

    data = np.array(data).reshape(1, -1)

    data_scaled = scaler.transform(data)

    prediction = model.predict(
        data_scaled
    )[0]

    probability = model.predict_proba(
        data_scaled
    )[0][1]

    return {
        "prediction": int(prediction),
        "fraud_probability": round(
            float(probability),
            6
        )
    }
