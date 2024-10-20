#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
    line = line.strip()
    match = re.match(r'^(\S+)\s', line)  # Simplified regex to match only the IP address
    if match:
        ip = match.group(1)  # Extract only the IP address
        print(f'{ip}\t1')  # Emit the IP address with a count of 1

