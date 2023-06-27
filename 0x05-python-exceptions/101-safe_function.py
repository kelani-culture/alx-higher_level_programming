#!/usr/bin/python3
import sys


def safe_function(fct, *args):

    try:
        n1, n2 = args
        result = fct(n1, n2)

    except (ZeroDivisionError, IndexError, TypeError, ValueError) as e:
        sys.stderr.write("Exceptions: ")
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        return None
    else:
        return result
