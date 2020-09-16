import pytest
import os
# import pandas as pd
from backend.core import settings
from backend.data.process_data import _clean_text, _spacy_tokenizer, parse_text
from backend.data import CORPUS

def test_corpus_pl():
    doc = CORPUS['pl']('test')


def test_clean_text_function():
    # test case 1
    case = '@anonymized_account @anonymized_account Brawo ty Daria kibic ma być na dobre i złe'
    output = 'Brawo ty Daria kibic ma być na dobre i złe'
    text_case = _clean_text(case)
    assert output == text_case
    # test case 2
    case = '@twitteraccount #k*** ty D1aria kibic ma być na dobre i złe 221431'
    output = 'ty Daria kibic ma być na dobre i złe'
    text_case = _clean_text(case)
    assert output == text_case


def test_spacy_tokenizer():
    # test case 1
    case = '@anonymized_account @anonymized_account Zapewne ci, co grali przez większość rundy w CLJ i nie ponieśli ani jednej porażki.'
    pre_out = _clean_text(case)
    output = 'grać większość runda ponieść jeden porażka'
    text_case = _spacy_tokenizer(CORPUS['pl'](pre_out))
    assert text_case == output
    # test case 2
    case = '@anonymized_account @account @anonymized_account Dlatego zaznaczyłem, że jest to wątpliwość. Nie wiem, czy w wieku 18 lat się jeszcze rośnie.'
    pre_out = _clean_text(case)
    output = 'zaznaczyłem wątpliwość wiedzieć wieko rosnąć'
    text_case = _spacy_tokenizer(CORPUS['pl'](pre_out))
    assert text_case == output
    # test case 3
    case = '@anonymized_account Żal ci biedaku??? Gdyby nie Kaczyński to by je twoi przyjaciele z PO rozkradl'
    pre_out = _clean_text(case)
    output = 'biedak kaczyński przyjaciel rozkradl'
    text_case = _spacy_tokenizer(CORPUS['pl'](pre_out))
    assert text_case == output