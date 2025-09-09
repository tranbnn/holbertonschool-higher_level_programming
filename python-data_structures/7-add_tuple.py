#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    fixed_tuple_a = 0
    fixed_tuple_n = 0

    if len(tuple_a) < 2:
        fixed_tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    else:
        fixed_tuple_a = tuple_a

    if len(tuple_b) < 2:
        fixed_tuple_b = tuple_b + (0,) * (2 - len(tuple_b))
    else:
        fixed_tuple_b = tuple_b

    first_elements = fixed_tuple_a[0] + fixed_tuple_b[0]
    second_elements = fixed_tuple_a[1] + fixed_tuple_b[1]

    return (first_elements, second_elements)
