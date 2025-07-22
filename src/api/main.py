from fastapi import FastAPI, Depends, HTTPException, Header
from src.api.schemas import CustomerFeatures, ChurnPrediction
from src.api.predictor import predict

app = FastAPI(title='Customer Churn Predictor')

API_TOKEN = "secret123"

def verify_token(authorization: str = Header(...)):
    if not authorization.startswith('Bearer '):
        raise HTTPException(status_code=403, detail='Invalid Token type')
    token = authorization.split(' ')[1]
    if token != API_TOKEN:
        raise HTTPException(status_code=403, detail='Invalid or missing token')

@app.get('/')
def root():
    return {'message': 'Welcome to the retail churn predictor !'}

@app.post('/predict', response_model=ChurnPrediction)
def predict_churn(customer: CustomerFeatures, auth=Depends(verify_token)):
    return predict(customer)

