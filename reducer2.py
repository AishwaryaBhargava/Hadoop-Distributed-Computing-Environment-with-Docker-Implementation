#!/usr/bin/env python

import sys

count = 0

for line in sys.stdin:
    line = line.strip()
    ip, _ = line.split('\t')  # We don't need the status code anymore, just the count
    if ip == '96.32.128.5':
        count += 1

print(count)

