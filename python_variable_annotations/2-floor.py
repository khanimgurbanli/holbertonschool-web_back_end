#!/usr/bin/env python3

"""
This module contains a function to compute the floor of a floating point number.
"""


def floor(n: float) -> int:
    """Return largest int value less than or equal to n
     :param n: float number
    :return: floor of n as an integer
    """
    return int(n) if n >= 0 else int(n) - 1
