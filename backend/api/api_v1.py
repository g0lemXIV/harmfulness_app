from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.schemas import TextCreate
from backend.core import settings
from backend.models import Predictor
from backend.core import validate_request
from backend.core.messages import HTTP_500_DETAIL


app = FastAPI(title="REST API for ML prediction for harmfulness twits",
              description="This is the REST API for the ML model for "
                          "Automatic cyberbullying detection",
              version="harmfulness_app: {}".format(settings.api_version),
              externalDocs={"poleval": "http://2019.poleval.pl/index.php/tasks/task6"}
              )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.post('/{}/predict'.format(settings.api_version))
async def post_prediction(text_in: TextCreate, authenticated: bool = Depends(validate_request)):

    # create predictor
    try:
        model = Predictor(model_name=settings.model_name, language=text_in.language,
                          min_length=settings.sentence_min_length)
    except:
        raise HTTPException(status_code=404, detail=HTTP_500_DETAIL)

    prediction = model.predict(text_in)
    return prediction
