# content of test_translate.py

from translate import *

def test_translate():
    assert translate(38) == "trentotto"
    assert translate(28) == "ventotto"
    assert translate(91) == "novantuno"
    assert translate(19) == "diciannove"
