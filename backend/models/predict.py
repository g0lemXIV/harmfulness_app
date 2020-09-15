import joblib
from langdetect import detect
from backend.models import model_lib
from backend.schemas import TextPredict, TextCreate
from backend.core.messages import NO_VALID_PAYLOAD, NO_VALID_LANGUAGE


class Predictor:

    def __init__(self, model_name: str, language='pl') -> None:
        self.model_name = model_name
        self.model = model_lib[model_name]
        self.language = language

    def predict(self, payload: TextCreate) -> TextPredict:
        """

        :param payload:
        :return:
        """
        if payload is None:
            raise ValueError(NO_VALID_PAYLOAD.format(payload))
        detect_lang = detect(payload.text)
        if (detect_lang != self.language) or (payload.language != self.language):
            raise ValueError(NO_VALID_LANGUAGE.format(payload.language, detect_lang))
        score = self.model.predict(payload.text)
        prediction = TextPredict(prediction=score,
                                 user_id=payload.user_id,
                                 time_utc=payload.time_utc,
                                 language=payload.language,
                                 text=payload.text,
                                 text_tokenized='TODO')
        return prediction
