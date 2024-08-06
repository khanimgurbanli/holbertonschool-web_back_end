#!/usr/bin/env python3

"""
This module contains functions for basic mathematical operations.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies its input by a given multiplier.
    Args:
        multiplier (float): The multiplier to use for multiplying input values.
    Returns:
        Callable[[float], float]: A function that takes a float as input and returns
        where the input is multiplied by the given multiplier.
    """

    def multiplier_function(value: float) -> float:

        return value * multiplier

    return multiplier_function
