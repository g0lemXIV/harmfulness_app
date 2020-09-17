import numpy as np
from langdetect import detect
from backend.models import model_lib
from backend.schemas import TextPredict, TextCreate
from backend.core.messages import NO_VALID_PAYLOAD, NO_VALID_LANGUAGE, NO_VALID_SENTENCE
from backend.data import parse_text


class Predictor:
    """Base class for generate prediction using sklearn models,
    in the next version it should be change to child class,
    and codding with some patterns."""

    def __init__(self, model_name: str, language="pl", min_length: int = 10) -> None:
        """
        :param model_name: name of the model loaded into model_lib in memory dict
        :param language: language to use
        :param min_length: minimum length of preprocessed text
        """
        self.model_name = model_name
        self.model = model_lib[model_name]
        self.language = language
        self.min_length = min_length

    def __str__(self):
        return self.__class__.__name__

    def predict(self, payload: TextCreate) -> TextPredict:
        """Function for predict new text data used in api.

        :param payload: TextCreate object created with pydantic
        :return:
            return pydantic TextPredict object with prediction,
            prediction probabilities, text, processed text, and
            additional information.
        """
        if payload is None:
            raise ValueError(NO_VALID_PAYLOAD.format(payload))
        detect_lang = detect(payload.text)
        if (detect_lang != self.language) or (payload.language != self.language):
            raise ValueError(NO_VALID_LANGUAGE.format(payload.language, detect_lang))
        # parse text
        text = parse_text(text=payload.text, language=payload.language)
        if not text or len(text) < self.min_length:
            raise ValueError(NO_VALID_SENTENCE.format(text, self.min_length, len(text)))
        # score model
        score = self.model.predict_proba([text])[0]
        score = np.around(score, decimals=4)
        prediction = TextPredict(
            prediction=np.argmax(score),
            prediction_proba=list(score),
            user_id=payload.user_id,
            time_utc=payload.time_utc,
            language=payload.language,
            text=payload.text,
            text_tokenized=text,
        )
        return prediction
