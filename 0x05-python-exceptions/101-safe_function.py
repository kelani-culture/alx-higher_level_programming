#!/usr/bin/python3
import sys


def safe_function(fct, *args):

    try:
        n1, n2 = args
        result = fct(n1, n2)

    except (ZeroDivisionError, IndexError, TypeError, ValueError) as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
    else:
        return result
