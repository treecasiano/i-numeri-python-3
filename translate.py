#!/usr/bin/env python
# coding: utf-8

import random
from numbers import *


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

print("-" * 40)
print("\nThis game tests your ability to write numbers up to 9999 in Italian.")
print("Random numbers will continue to be generated until you use ctrl + C to exit.")
print("\nYou will need to activate the US-Extended (Mac) or Windows International (PC) Keyboard.")
print("For an acute accent(é):")
print("\t[MAC]\t\ttype option + e and then the vowel")
print("\t[WINDOWS]\ttype single quote and then the vowel\n")
print("-" * 40)

while(True):
    number = random.randint(1, 10000)
    translation = translate_number(number)
    print("\nWhat is " + str(number) + " in Italian?")
    answer = input(">> ")
    if answer.lower() == translation:
        print("Correct! Let's try another number.\n")
    else:
        print("That is not correct. The answer is " + translation + ".")