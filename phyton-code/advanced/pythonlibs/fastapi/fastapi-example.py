

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PredictionRequest(BaseModel):
    amount: float
    country: str


@app.post("/predict")
def predict(data: PredictionRequest):
    risk = "high" if data.amount > 10000 else "low"
    return {"risk": risk}
