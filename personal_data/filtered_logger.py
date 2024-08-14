#!/usr/bin/python3
""" Basic Dictionary: The function should use a regex to replace occurrences of certain field values
"""

import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Hide log message"""
    pattern = f"({'|'.join(fields)})=.+?{separator}"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}{separator}", message)
