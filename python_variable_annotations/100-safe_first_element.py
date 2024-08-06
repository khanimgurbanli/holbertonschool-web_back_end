#!/usr/bin/env python3
""" Details: Augment the follow code the correct
                 duck type annotation
    Argument: lst: Sequence[Any]
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of lst that there is any otherwise None"""
    if lst:
        return lst[0]
    else:
        return None
