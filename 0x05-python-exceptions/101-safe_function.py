#!/usr/bin/python3
import sys


def safe_function(fct, *args):

    try:
        n1, n2 = args
        result = fct(n1, n2)

    except (ZeroDivisionError, IndexError, TypeError) as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
    except ValueError:
        fct()
        return None
    else:
        return result
