from fastapi import FastAPI
from config import app_config
from preprocess import fake_news_preprocess
from models import model
from payloads import FakeNewsPayload

app = FastAPI(**app_config)

@app.post('/predict/')
async def predict(payload: FakeNewsPayload):
    vector = fake_news_preprocess(payload)
    prediction = model.predict(vector)
    
    real_probability = float(prediction[0][0])
    fake_probability = 1 - real_probability
    
    response = {
        'fake_probability': fake_probability
    }
    
    return response