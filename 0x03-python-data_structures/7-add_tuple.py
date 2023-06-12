#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 0:
        a = tuple_b[0] + 0
        b = tuple_b[1] + 0
        return (a, b)
    elif len(tuple_b) == 0:
        a = tuple_a[0] + 0
        b = tuple_a[1] + 0
        return (a, b)
    if len(tuple_a) == 2 and len(tuple_b) == 2:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]
        return(a, b)
    elif len(tuple_a) == 2 and len(tuple_b) < 2:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + 0
        return (a, b)
    elif len(tuple_b) == 2 and len(tuple_b) < 2:
        a = tuple_a[0] + tuple_b[0]
        b = 0 + tuple_b[1]
        return (a, b)
    elif len(tuple_a) > 2 or len(tuple_b) > 2:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]
        return (a, b)
