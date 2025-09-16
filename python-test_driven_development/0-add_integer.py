#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    add_integer: Adds two integers

    Args:
        a: The first input integer
        b: The second input integer, default is 98

    Returns:
    The sum of a and b as ints. a and b will be casted
    into ints if not already.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
