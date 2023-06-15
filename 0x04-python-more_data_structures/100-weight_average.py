#!/usr/bin/python3

def weight_average(my_list=[]):

    if len(my_list) == 0:
        return 0
    avg_w = sum([x * y for x, y in my_list]) / sum([x[1] for x in my_list])
    return avg_w
