#!/usr/bin/env python

import sys

ip_counts = {}

for line in sys.stdin:
    line = line.strip()
    ip, _ = line.split('\t')  # Since the mapper emits a count of 1, you can ignore the second part
    ip_counts[ip] = ip_counts.get(ip, 0) + 1  # Increment the count for the IP

max_ip = max(ip_counts, key=ip_counts.get)  # Find the IP with the maximum count
max_count = ip_counts[max_ip]  # Get the count for the most frequent IP

print(f'Most frequent IP: {max_ip}\nNumber of accesses: {max_count}')

