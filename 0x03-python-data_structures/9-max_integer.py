#!/usr/bin/python3

def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None
    largest = 0

    for number in my_list:
        if number > largest:
            largest = number
    return largest
