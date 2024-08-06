#!/usr/bin/env python3

from typing import Mapping, TypeVar, Any, Union

# Define a type variable that can be any type
T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """
    Safely get the value from the dictionary by key. Return the default value if the key is not found.

    Args:
        dct (Mapping[Any, T]): A dictionary-like object where keys can be of any type and values are of type T.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None]): The default value to return if the key is not found. Can be of type T or None.

    Returns:
        Union[T, None]: The value corresponding to the key if it exists, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
