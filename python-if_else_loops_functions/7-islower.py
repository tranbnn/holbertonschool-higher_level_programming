#!/usr/bin/python3

def islower(c):
    if ord(c) >= 97 and ord(c) <= 173:
        return "True"

    elif ord(c) >= 65 and ord(c) <= 91:
        return "False"
    else:
        return "idk"
