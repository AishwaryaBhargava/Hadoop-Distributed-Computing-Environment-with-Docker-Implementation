#!/usr/bin/env python

import sys
import re

# List of standard HTTP methods to check against
http_methods = set(['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH', 'TRACE', 'CONNECT'])

for line in sys.stdin:
    line = line.strip()
    match = re.match(r'^\S+\s+\S+\s+\S+\s+\[.*?\]\s+"(\S+)', line)
    if match:
        method = match.group(1).upper()  # Convert to uppercase to standardize the output
        if method in http_methods:
            print(f'{method}\t1')

