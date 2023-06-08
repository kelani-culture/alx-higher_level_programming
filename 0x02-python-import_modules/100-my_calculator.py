#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":

    argvs = sys.argv
    argc = len(argvs)

    if (argc - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argvs[1])
    b = int(argvs[3])

    if argvs[2] == '+':
        print("{0} + {1} = {2}".format(a, b, add(a, b)))

    elif argvs[2] == '-':
        print("{0} - {1} = {2}".format(a, b, sub(a, b)))

    elif argvs[2] == '/':
        print("{0} / {1} = {2}".format(a, b, div(a, b)))

    elif argvs[2] == '*':
        print("{0} * {0} = {2}".format(a, b, mul(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
