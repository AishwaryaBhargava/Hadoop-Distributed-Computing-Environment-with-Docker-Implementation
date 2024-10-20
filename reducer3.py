#!/usr/bin/env python

import sys

methods = set()

for line in sys.stdin:
    line = line.strip()
    method, _ = line.split('\t')  # Ignore the count, we just need the method
    methods.add(method)

print(f'Total unique methods: {len(methods)}')
print(f'Methods: {", ".join(methods)}')

