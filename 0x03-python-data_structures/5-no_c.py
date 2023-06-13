#!/usr/bin/python3

def no_c(my_string):

    count = 0
    char = ""
    while count < len(my_string):
        if (my_string[count] != 'c') and (my_string[count] != 'C'):
            char += my_string[count]
        count += 1
    return char
