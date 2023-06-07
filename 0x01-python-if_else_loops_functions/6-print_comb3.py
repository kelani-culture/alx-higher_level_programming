#!/usr/bin/python3

for i in range(48, 58):
    for j in range(48, 58):
        if (i != j and j != i) and (i < j):
            if (chr(i) != '8') or (chr(j) != '9'):
                print("{:c}".format(i), end="")
                print("{:c}, ".format(j), end="")
            else:
                print("{:c}{:c}".format(i, j))
                break
