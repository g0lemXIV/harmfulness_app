import spacy
from .config import settings
from .security import validate_request


CORPUS = {"pl": spacy.load(settings.spacy_corpus)}
