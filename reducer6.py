#!/usr/bin/env python

import sys

count = 0

for line in sys.stdin:
    line = line.strip()
    method, value = line.split('\t')
    if method == "POST":
        count += int(value)

print(f'Total POST requests: {count}')

