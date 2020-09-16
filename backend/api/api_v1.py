from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import TextCreate
from backend.core import settings
from backend.models import Predictor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.post('/v1/predict/{}'.format(settings.model_name))
def create_prediction(text_in: TextCreate):
    pass