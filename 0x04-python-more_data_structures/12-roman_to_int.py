#!/usr/bin/python3
from functools import reduce

def roman_to_int(roman_string):
    if (roman_string == None) or len(roman_string) == 0:
        return 0
    roman_letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_num = [roman_letters.get(i) for i in roman_string]

    decimal = reduce(lambda x, y: x + y if y <= x else y - x, roman_num)
    return decimal
