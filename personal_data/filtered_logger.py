#!/usr/bin/python3
""" Regex-ing, Log formatter, Create logger, Connect to secure database,
    Read and filter data """
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Description: Writed a function called filter_datum that
                 returns the log message obfuscated"""
    for field in fields:
        return re.sub(f"({'|'.join(field)})=.+?{separator}",
                      r"\1=" + redaction + separator, message)
