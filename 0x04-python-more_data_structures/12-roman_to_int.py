#!/usr/bin/python3
from functools import reduce

def roman_to_int(roman_string):
    if isinstance(roman_string, str) == False or (roman_string == None):
        return 0
    roman_letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_num = [roman_letters.get(i) for i in roman_string]

    decimal = reduce(lambda x, y: x + y if y <= x else x - y, roman_num)
    return decimal
