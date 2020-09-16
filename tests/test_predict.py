import pytest
from backend.core import settings
from backend.models import Predictor
from backend.schemas import TextCreate, TextPredict
from backend.data import parse_text

def test_predictior_loader():
    # test prediction loader
    test_predictor = Predictor(settings.model_name)
    assert test_predictor.model_name == settings.model_name
    assert test_predictor.language == 'pl'
    assert test_predictor.min_length == 10
    assert test_predictor.model


def test_predictor_predict():
    test_predictor = Predictor(settings.model_name)

    # test true case
    test_case = TextCreate(text='Dla mnie faworytem do tytułu będzie Cracovia. Zobaczymy, czy typ się sprawdzi.')
    result = test_predictor.predict(test_case)
    assert isinstance(result, TextPredict)
    assert(result.text == test_case.text)

    # integration test
    integration_case = parse_text(test_case.text, 'pl')
    assert(result.text_tokenized == integration_case)

    # test payload None
    with pytest.raises(ValueError):
        result = test_predictor.predict(None)
        assert isinstance(result, TextPredict)

    # test bad case
    with pytest.raises(ValueError):
        test_case = TextCreate(text='test')
        result = test_predictor.predict(test_case)
        assert isinstance(result, TextPredict)

    # test bad case with wrong language
    with pytest.raises(ValueError):
        test_case = TextCreate(text='this is my test')
        result = test_predictor.predict(test_case)
        assert isinstance(result, TextPredict)

    # test validmodel with length
    with pytest.raises(ValueError):
        test_case = TextCreate(text='test')
        result = test_predictor.predict(test_case)
        assert isinstance(result, TextPredict)



