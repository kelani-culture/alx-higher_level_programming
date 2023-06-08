#!/usr/bin/python3
import sys

argvs = sys.argv
argc = len(argvs)

if (argc == 1):
    print(0)

else:
    count = 0
    for argv in argvs[1:]:
        int_argv = int(argv)
        count += int_argv
    print(count)
