import re
from backend.core import CORPUS


def _clean_text(text: str) -> str:
    """Text cleaner from raw string, function checks if words
    contain digits and special characters
    :param text: string contains words to clean
    :return:
        clean text
    """
    text = re.sub(r"\d+", "", text)
    text = " ".join(w for w in text.split() if "@" not in w and "#" not in w)
    return text


def _spacy_tokenizer(my_tokens: object) -> str:
    """Function clean text with spacy wrapper, it uses polish language
    corpus. Drop punctuation, polish stop words, currency, numbers and emails
    :param my_tokens: string loaded with spacy pipeline
    :return:
        clean text with lower case lemmas
    """
    # basic checking
    my_tokens = [
        word
        for word in my_tokens
        if not word.is_punct
        and not word.is_stop
        and len(word) > 3
        and not word.like_num
        and not word.is_currency
        and not word.like_email
    ]
    # Lemmatization
    my_tokens = [
        word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_
        for word in my_tokens
    ]
    # make string from tokens
    my_tokens = " ".join(i for i in my_tokens)
    return my_tokens


def parse_text(text: str, language: str = "pl") -> str:
    """Main function for text preprocessing before enters it to pipeline.
    First clean raw string text, then uses spacy and polish corpus for
    cleaning process.
    :param text: raw string with text
    :param language: corpus language (default pl)
    :return:
        Function returns preprocessed string
    """
    text = _clean_text(text)
    # load text as spacy document
    doc = CORPUS[language](text)
    # preprocess data with same pipeline as in experiment
    output = _spacy_tokenizer(doc)
    return output
