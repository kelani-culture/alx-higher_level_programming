#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    try:
        count = 0
        while count < x and x != 0:
            print(my_list[count], end="")
            count += 1
        print()
    except:
        print()
        return count 
    else:
        return x
