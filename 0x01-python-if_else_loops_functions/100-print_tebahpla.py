#!/usr/bin/python3

lower = 122
upper = 89

while lower >= 97 or upper >= 65:
    print("{:c}{:c}".format(lower, upper), end="")
    lower -= 2
    upper -= 2
