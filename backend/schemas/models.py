"""Create models for input and output receiver"""
from typing import Optional, List
from pydantic import BaseModel


class TextBase(BaseModel):
    user_id: Optional[str] = None
    time_utc: Optional[str] = None
    language: Optional[str] = "pl"


class TextCreate(TextBase):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "to jest mój pierwszy test",
                "user_id": 1,
                "time_utc": "2020-09-20 20:00:00",
                "language": "pl",
            }
        }


class TextPredict(TextBase):
    prediction: float
    prediction_proba: List[float]
    text: str
    text_tokenized: str

    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "time_utc": "2020-09-20 20:00:00",
                "language": "pl",
                "prediction": 0,
                "prediction_proba": [0.9, 0.1, 0.0],
                "text": "Dla mnie faworytem do tytułu będzie Cracovia. "
                "Zobaczymy, czy typ się sprawdzi.",
                "text_tokenized": "faworyt tytuł cracovia zobaczyć sprawdzić",
            }
        }
