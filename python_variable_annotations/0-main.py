#!/usr/bin/env python3
import math

fl = __import__('3-to_str').to_str

print(fl(25.9202) == str(25.9202))
print(fl.__annotations__)
