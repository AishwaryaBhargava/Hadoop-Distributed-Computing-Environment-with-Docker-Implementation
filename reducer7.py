#!/usr/bin/env python

import sys

count = 0

for line in sys.stdin:
    line = line.strip()
    ip, status = line.split('\t')
    if status == '404':
        count += 1

print(count)
