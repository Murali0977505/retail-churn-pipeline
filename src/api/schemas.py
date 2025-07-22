from pydantic import BaseModel

class CustomerFeatures(BaseModel):
    
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: str
    TotalCharges: float

class ChurnPrediction(BaseModel):

    churn_probability: float
    churn: bool
