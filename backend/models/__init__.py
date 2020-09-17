import os

# import predictor
import joblib
from backend.core import settings

# load model before add it to pipeline
models_pth = os.path.join(os.path.dirname(__file__), "models_pkl")

# first experiment model path
exp0_pth = os.path.join(models_pth, "{}.sav".format(settings.model_name))

model_lib = dict()
model_lib[settings.model_name] = joblib.load(exp0_pth)


from .predict import Predictor
