#!/usr/bin/env python
# coding: utf-8

from translate import *


def test_translate():
    assert translate_number(8) == "otto"
    assert translate_number(10) == "dieci"
    assert translate_number(38) == "trentotto"
    assert translate_number(91) == "novantuno"
    assert translate_number(19) == "diciannove"
    assert translate_number(100) == "cento"
    assert translate_number(101) == "centouno"
    assert translate_number(108) == "centotto"
    assert translate_number(111) == "centoundici"
    assert translate_number(283) == "duecentottantatré"
    assert translate_number(400) == "quattrocento"
    assert translate_number(345) == "trecentoquarantacinque"
    assert translate_number(817) == "ottocentodiciassette"
    assert translate_number(999) == "novecentonovantanove"
