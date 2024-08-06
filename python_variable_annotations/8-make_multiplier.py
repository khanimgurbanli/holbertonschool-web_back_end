#!/usr/bin/env python3

"""
This module contains a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns:
        Callable[[float], float]: A function that takes a float and returns it multiplied by the multiplier.
    """
    return lambda x: x * multiplier
