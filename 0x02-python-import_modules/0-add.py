#!/usr/bin/python3

if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b, __import__('add_0').add(a, b))))
