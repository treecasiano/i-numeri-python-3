#!/usr/bin/env python
# coding: utf-8

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
    # the commented out code below is slow because it rehashes
    # for key in nums_to_twenty:
    #     if str(num) == key:
    #         translated_num = nums_to_twenty[key]
    #         return translated_num
    for k, v in nums_to_twenty.items():
        if str(num) == k:
            translated_num = v
            return translated_num


def translate_20_to_99(num):
    ones_place = str(num)[1]
    tens_place = str(num)[0]

    # get the translation of the ones place
    if ones_place == "3":
        ones_place = "tré"
    else:
        for k, v in nums_to_twenty.items():
            if ones_place == k:
                ones_place = v

    # get the translation of the tens place
    for k, v in tens_place_nums.items():
        if tens_place == k:
            translated_num = v + ones_place

            if ones_place == "0":
                translated_num = v

            if ones_place == "uno" or ones_place == "otto":
                translated_num = v[0:-1] + ones_place

            return translated_num


def translate_100_to_999(num):
    hundreds_place = str(num)[0]
    tens_place = str(num)[1]
    ones_place = str(num)[2]
    rest_of_number = int(str(num)[1:])

    if int(hundreds_place) > 1:
        hundreds = translate_to_20(num//100) + "cento"
    else:
        hundreds = "cento"

    # obtain value of the tens and ones place
    # the "o" ending of cento is dropped if followed by otto or ottanta
    if tens_place == "0" and ones_place == "0":
        translated_num = hundreds
        return translated_num

    if rest_of_number < 20:
        if rest_of_number == 8:
            hundreds = hundreds[0:-1]
        translated_num = hundreds + translate_to_20(rest_of_number)
        return translated_num

    if rest_of_number >= 20:
        if tens_place == "8":
            hundreds = hundreds[0:-1]
        translated_num = hundreds + translate_20_to_99(rest_of_number)
        return translated_num


def translate_1000_to_9999(num):
    thousands_place = str(num)[0]
    rest_of_number = int(str(num)[1:])

    if thousands_place == "1":
        thousands = "mille"

    if int(thousands_place) >= 2:
        thousands = translate_to_20(int(thousands_place)) + "mila"

    if rest_of_number == 0:
        translated_num = thousands
        return translated_num
    elif rest_of_number >= 100:
        translated_num = thousands + translate_100_to_999(rest_of_number)
        return translated_num
    elif rest_of_number >= 20:
        translated_num = thousands + translate_20_to_99(rest_of_number)
        return translated_num
    else:
        translated_num = thousands + translate_to_20(rest_of_number)
        return translated_num


def translate_number(num):
    if num < 20:
        translated_num = translate_to_20(num)
    elif 20 <= num < 100:
        translated_num = translate_20_to_99(num)
    elif 100 <= num < 1000:
        translated_num = translate_100_to_999(num)
    else:
        translated_num = translate_1000_to_9999(num)
    return translated_num


