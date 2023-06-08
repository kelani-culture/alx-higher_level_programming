#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argvs = sys.argv
    len_argv = len(argvs)

    if len_argv == 1:
        print("0 arguments.")

    else:
        count = 1
        print(f"{len_argv - 1} argument:" if len_argv == 2 else f"{len_argv - 1} arguments:")
        for argv in argvs[1:]:
            print(f"{count}: {argv}")
            count += 1
