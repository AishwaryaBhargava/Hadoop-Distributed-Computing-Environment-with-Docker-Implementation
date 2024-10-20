#!/usr/bin/env python

import sys

ip_sizes = {}

for line in sys.stdin:
    line = line.strip()
    ip, size = line.split('\t')
    if ip in ip_sizes:
        ip_sizes[ip] += int(size)
    else:
        ip_sizes[ip] = int(size)

sorted_ips = sorted(ip_sizes, key=ip_sizes.get, reverse=True)

for ip in sorted_ips[:3]:
    print(f'{ip}\t{ip_sizes[ip]}')
