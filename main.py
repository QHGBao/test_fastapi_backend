from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

class House(BaseModel):
    area: float
    rooms: int

@app.post("/predict")
def predict(date: House):
    features = [[date.area, date.rooms]]
    prediction = model.predict(features)    
    return {"price": prediction[0]}