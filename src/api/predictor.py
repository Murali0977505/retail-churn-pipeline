import joblib
import numpy as np
import os
from src.api.schemas import CustomerFeatures

model_path = os.getenv('MODEL_PATH', 'model.pkl')
model = joblib.load(model_path)

def preprocess(features: CustomerFeatures):
    df = [list(features.dict().values())]
    return np.array(df)

def predict(features: CustomerFeatures):
    processed = preprocess(features)
    probability = model.predict_proba(processed)[0][1]
    return{
        "churn_probability": probability,
        "churn": probability > 0.5
    }

