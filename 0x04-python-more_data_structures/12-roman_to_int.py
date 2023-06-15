#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or isinstance(roman_string, str) is False:
        return 0

    roman_dict  = {'I': 1, 'V': 5, 'X': 10, 'L': 50,\
'C': 100, 'D': 500, 'M': 1000}

    roman_num = [roman_dict.get(i) for i in roman_string.upper()]

    rev_num = list(reversed(roman_num))
    right_val = rev_num[0]

    decimal = 0
    for i in rev_num:
        left_val = i

        if left_val < right_val:
            decimal -= left_val
        else:
            decimal += left_val
        right_val = left_val
    return decimal
