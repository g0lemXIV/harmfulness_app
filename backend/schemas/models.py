"Create models for input and output reciver"
from typing import Optional, List
from pydantic import BaseModel


class TextBase(BaseModel):
    user_id: Optional[str] = None
    time_utc: Optional[str] = None
    language: Optional[str] = None


class TextCreate(TextBase):
    text: str


class TextPredict(TextBase):
    prediction: float
    prediction_proba: List[float]
    text: str
    text_tokenized: str

