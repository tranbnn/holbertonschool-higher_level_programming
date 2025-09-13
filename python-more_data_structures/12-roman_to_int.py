#!/usr/bin/python3
def roman_to_int(roman_string):

    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000}

    int_val = 0
    prev_val = 0

    for c in reversed(roman_string):
        current_val = roman_num.get(c, 0)

        if current_val == 0:
            return 0

        if current_val < prev_val:
            int_val -= current_val
        else:
            int_val += current_val

        prev_val = current_val

    return int_val
