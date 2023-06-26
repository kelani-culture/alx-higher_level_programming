#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length

    for idx in range(list_length):
        try:
            result[idx] = my_list_1[idx] / my_list_2[idx]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            result[idx] = 0
            print("division by 0")
        except TypeError:
            result[idx] = 0
            print("wrong type")
        finally:
            pass
    return result
