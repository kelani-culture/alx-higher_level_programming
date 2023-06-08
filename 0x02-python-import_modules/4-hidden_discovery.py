#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    hidden = dir(hidden_4)
    for ind in hidden:
        if ind[0] != "_":
            print(ind)
