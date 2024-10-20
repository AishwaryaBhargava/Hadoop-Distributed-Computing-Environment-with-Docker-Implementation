#!/usr/bin/env python
import sys
import re

# This pattern will match the request line regardless of the HTTP method used
pattern = re.compile(r'\"[A-Z]+\s(.*?)\sHTTP\/[0-9\.]+"')

for line in sys.stdin:
    line = line.strip()
    match = pattern.search(line)
    if match:
        # Extract the path
        path = match.group(1)
        # Emit the path and a count of 1
        print(f"{path}\t1")

