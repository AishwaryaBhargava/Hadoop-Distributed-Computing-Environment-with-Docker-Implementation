#!/usr/bin/env python

import sys

total_size = 0

for line in sys.stdin:
    line = line.strip()
    ip, size = line.split('\t')
    total_size += int(size)

print(total_size)
