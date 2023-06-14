#!/usr/bin/python3

def search_replace(my_list, search, replace):

    list_r = [i for i in my_list]

    count = 0
    for i in list_r:
        if i == search:
            list_r[count] = replace
        count += 1
    return list_r
