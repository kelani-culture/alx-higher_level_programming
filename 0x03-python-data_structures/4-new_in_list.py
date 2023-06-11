#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = []
    count = 0

    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list

    while count < len(my_list):
        new_list.append(my_list[count])
        count += 1
    new_list[idx] = element
    return new_list
