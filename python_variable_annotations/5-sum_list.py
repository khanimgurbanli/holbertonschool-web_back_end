#!/usr/bin/env python3
"""
This module contains functions for summing up a list of floating-point numbers.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Sums up the floating-point numbers in a list and returns the result.

    Parameters:
    input_list (List[float]): The list of floating-point numbers to be summed.

    Returns:
    float: The sum of the numbers in the list.
    """
    return sum(input_list)
