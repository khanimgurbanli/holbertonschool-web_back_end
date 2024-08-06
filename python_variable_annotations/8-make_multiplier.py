#!/usr/bin/env python3

"""This module contains a function to create a multiplier function."""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies its input by a given multiplier.

    Args:
        multiplier (float): The multiplier to use for multiplying input values.

    Returns:
        Callable[[float], float]: A function that takes a float as input and returns a float,
                                   where the input is multiplied by the given multiplier.
    """

    def multiplier_function(value: float) -> float:
        """
        Multiplies the given value by the multiplier.

        Args:
            value (float): The value to be multiplied.

        Returns:
            float: The result of multiplying the input value by the multiplier.
        """
        return value * multiplier

    return multiplier_function

