#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        sys.stderr.write("Exception: Unknown format code 'd' for object of type 'str'\n")
        return False
    else:
        return True
