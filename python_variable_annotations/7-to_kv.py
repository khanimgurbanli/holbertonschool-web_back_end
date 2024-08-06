#!/usr/bin/env python3

"""This module contains a function to sum up a list of integers and floating-point numbers."""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple where the first element is the string `k` and the second element
    is the square of the integer or float `v`.

    Parameters:
    k (str): The key as a string.
    v (Union[int, float]): The value to be squared; can be an integer or a float.

    Returns:
    Tuple[str, float]: A tuple where the first element is `k` and the second element
                       is the square of `v` as a float.
    """
    return (k, float(v ** 2))
