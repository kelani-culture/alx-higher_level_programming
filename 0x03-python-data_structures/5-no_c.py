#!/usr/bin/python3

def no_c(my_string):

    count = 0

    while count < len(my_string) - 1:
        if (my_string[count] == 'c') or (my_string[count] == 'C'):
            my_string = my_string[:count] + my_string[count + 1:]
        count += 1
    return my_string
