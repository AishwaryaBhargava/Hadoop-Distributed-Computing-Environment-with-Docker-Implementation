#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
    line = line.strip()
    match = re.match(r'^(\S+)\s+\S+\s+\S+\s+\[16/Jan/2022:.*?\]\s+".*?"\s+(\d+)\s+(\d+|-).*$', line)
    if match:
        ip, status, size = match.groups()
        if status == '200' and size != '-':
            print(size)
