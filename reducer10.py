#!/usr/bin/env python

import sys

total_size = 0

for line in sys.stdin:
    line = line.strip()
    size = int(line)
    total_size += size

print(total_size)
