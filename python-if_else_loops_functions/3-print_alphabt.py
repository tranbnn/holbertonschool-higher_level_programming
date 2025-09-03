#!/usr/bin/python3

for i in range(97, 123):
    if "{:s}".format(chr(i)) == "e" or "{:s}".format(chr(i)) == "q":
        continue
    print("{:s}".format(chr(i)), end="")
