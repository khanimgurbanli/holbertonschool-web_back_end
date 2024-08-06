#!/usr/bin/env python3
"""
This module contains a function to sum up a list of integers and floating-point numbers.
"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Sums up the numbers in a list, where the list can contain both integers and floating-point numbers.

        Parameters:
        mxd_lst (List[Union[int, float]]): The list of integers and/or floating-point numbers to be summed.

        Returns:
        float: The sum of the numbers in the list.
        """
    return float(sum(mxd_lst))