import os
from backend.core import settings
import joblib
# load model before add it to pipeline
model_lib = dict()
model_lib[settings.model_name] = joblib.load(os.path.join('./models_pkl'),
                                             "{}.sav".format(settings.model_name))


# import predictor
from .predict import Predictor