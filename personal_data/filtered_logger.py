#!/usr/bin/python3

import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Description: Writed a function called filter_datum that
                 returns the log message obfuscated:

    Arguments:
        fields: a list of strings all fields to obfuscate
        redaction: a string by what the field will be
                   obfuscated
        message: a string the log line
        separator: a string  by which character is
                       separating all fields in the log line (message)
    The function should use a regex to replace occurrences of certain
    field values.
    filter_datum should be less than 5 lines long and use re.sub to
    perform the substitution with a single regex.
    """
    pattern = f"({'|'.join(fields)})=.+?{separator}"
    return re.sub(pattern, r"\1=" + redaction + separator, message)
