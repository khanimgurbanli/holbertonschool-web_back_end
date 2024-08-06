#!/usr/bin/env python3

"""This module contains a function to create a multiplier function."""

from typing import Sequence, Optional, Any

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Return the first element of the sequence if it exists, otherwise return None.

    Args:
        lst (Sequence[Any]): A sequence (list, tuple, etc.) of any type of elements.

    Returns:
        Optional[Any]: The first element of the sequence if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
