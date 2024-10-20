#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
    line = line.strip()
    match = re.match(r'^(\S+)\s+\S+\s+\S+\s+\[19/Dec/2020:.*?\]\s+".*?"\s+(\d+)\s+(\d+|-).*$', line)
    if match:
        ip, status, size = match.groups()
        if size != '-':
            print(f'{ip}\t{size}')
