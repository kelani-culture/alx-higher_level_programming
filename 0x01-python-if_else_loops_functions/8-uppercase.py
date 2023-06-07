#!/usr/bin/python3


def uppercase(str):

    upper_case = ""

    for (i in str):
        if (ord(i) >= 65 and ord(i) <= 90)
            upper_case += i
        
        elif (ord(i) > 90)
            to_upper = ord(i) - (ord('a') - ord('A'))
            upper_case += chr(to_upper)

        elif (i == ' '):
            upper_case += ' '

        else:
            upper_case += i
    print("{}".format(upper_case))
