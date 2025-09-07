#!/usr/bin/python3
import sys

i = 0

if __name__ == "__main__":

    for i in range(1, len(sys.argv)):
        if i == 0:
            print("0 arguments.")
        elif i  == 1:
            print("1 argument:")
            print(f"{i}: {sys.argv[i]}")
        else:
            print(f"{i} arguments: {sys.argv[i]}")
            for i in range(1, len(sys.argv)):
                print(f"{i}: {sys.argv[i]}")
