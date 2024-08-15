#!/usr/bin/python3
""" Regex-ing, Log formatter, Create logger, Connect to secure database,
    Read and filter data """

PII_FIELDS = ("name", "email", "phone", "ssn", "password")
""" containing the fields from user_data.csv that are considered PII. """

import re
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Description: Writed a function called filter_datum that
                 returns the log message obfuscated"""
    return re.sub(
        f"({'|'.join(fields)})=.+?{separator}", r"\1=" + redaction + separator, message
    )
