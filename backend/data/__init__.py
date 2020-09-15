from backend.core import settings
import spacy


CORPUS = {'pl': spacy.load(settings.spacy_corpus)}