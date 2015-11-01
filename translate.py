#!/usr/bin/env python
# coding: utf-8
import random

nums_to_twenty = {
    '1': 'uno',
    '2': 'due',
    '3': 'tre',
    '4': 'quattro',
    '5': 'cinque',
    '6': 'sei',
    '7': 'sette',
    '8': 'otto',
    '9': 'nove',
    '10': 'dieci',
    '11': 'undici',
    '12': 'dodici',
    '13': 'tredici',
    '14': 'quattordici',
    '15': 'quindici',
    '16': 'sedici',
    '17': 'diciassette',
    '18': 'diciotto',
    '19': 'diciannove',
}

tens_place_nums = {
    '2': 'venti',
    '3': 'trenta',
    '4': 'quaranta',
    '5': 'cinquanta',
    '6': 'sessanta',
    '7': 'settanta',
    '8': 'ottanta',
    '9': 'novanta'
}


def translate_to_20(num):
    for key in nums_to_twenty:
        if str(num) == key:
            translated_num = nums_to_twenty[key]
            return translated_num


def translate_20_to_99(num):
    ones_place = str(num)[1]
    tens_place = str(num)[0]

    # get the translation of the ones place
    if ones_place == "3":
        ones_place = "tré"
    else:
        for key in nums_to_twenty:
            if ones_place == key:
                ones_place = nums_to_twenty[key]

    # get the translation of the tens place
    for key in tens_place_nums:
        if tens_place == key:
            translated_num = tens_place_nums[key] + ones_place

            if ones_place == "0":
                translated_num = tens_place_nums[key]

            if ones_place == "uno" or ones_place == "otto":
                translated_num = tens_place_nums[key][0:-1] + ones_place

            return translated_num


def translate(num):
    if num <= 20:
        translated_num = translate_to_20(num)
    else:
        translated_num = translate_20_to_99(num)
    return translated_num

print (translate(28))
