#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argvs = sys.argv
    len_argv = len(argvs) - 1

    if len_argv == 0:
        print("0 arguments.")

    else:
        count = 1
        if len_argv == 1:
            print(f"{len_argv} argument:")
        else:
            print(f"{len_argv} arguments:")
        for argv in argvs[1:]:
            print(f"{count}: {argv}")
            count += 1
