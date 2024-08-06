#!/usr/bin/env python3
import math

concat = __import__('2-floor').floor

print(concat(25.9202) == math.floor(25.9202))
print(concat.__annotations__)
