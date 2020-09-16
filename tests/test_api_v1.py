import pytest
from fastapi.testclient import TestClient
from backend.api.api_v1 import app
from backend.core import settings, messages
# load api to the test client
client = TestClient(app)


def test_post_prediction_token():
    # no key test case
    response = client.post('/{}/predict'.format(settings.api_version))
    assert response.status_code == 400
    assert response.json() == {"detail": messages.NO_API_KEY}
    # wrong key test case
    response = client.post(
        '/{}/predict'.format(settings.api_version),
        json={"text": "test"},
        headers={"token": "WRONG_TOKEN"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": messages.AUTH_REQ}


def test_post_wrong_payload():

    # payload is none
    response = client.post(
        '/{}/predict'.format(settings.api_version),
        json={},
        headers={"token": settings.auth_key}
    )
    assert response.status_code == 422

    # payload in different language
    response = client.post(
        '/{}/predict'.format(settings.api_version),
        json={'text': 'this is test'},
        headers={"token": settings.auth_key}
    )
    assert response.status_code == 422

    # payload too short
    response = client.post(
        '/{}/predict'.format(settings.api_version),
        json={'text': 'mój test'},
        headers={"token": settings.auth_key}
    )
    assert response.status_code == 422

    # payload with text only
    test_text = 'Dla mnie faworytem do tytułu będzie Cracovia. Zobaczymy, czy typ się sprawdzi.'
    response = client.post(
        '/{}/predict'.format(settings.api_version),
        json={"text": test_text},
        headers={"token": settings.auth_key}
    )
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert "prediction_proba" in response.json()
    assert "text_tokenized" in response.json()

    # additional check
    test_response = response.json()
    assert len(test_response["prediction_proba"]) == 3
    assert test_response["prediction"] == 0
    assert test_response["text"] == test_text
    assert test_response["text_tokenized"] == 'faworyt tytuł cracovia zobaczyć sprawdzić'

    # full payload
    response = client.post(
        '/{}/predict'.format(settings.api_version),
        json={"text": test_text,
              'user_id': 1,
              'time_utc': '2020-09-20 20:00:00',
              'language': 'pl'},
        headers={"token": settings.auth_key}
    )
    assert response.status_code == 200
    test_response = response.json()
    assert test_response['user_id'] == 1
    assert test_response['language'] == 'pl'
    assert test_response['time_utc'] == '2020-09-20 20:00:00'

