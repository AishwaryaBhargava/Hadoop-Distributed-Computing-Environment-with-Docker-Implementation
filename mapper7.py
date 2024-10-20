#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
    line = line.strip()
    match = re.match(r'^(\S+)\s+\S+\s+\S+\s+\[.*?\]\s+".*?"\s+(\d+)\s+.*$', line)
    if match:
        ip, status = match.groups()
        print(f'{ip}\t{status}')

