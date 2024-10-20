#!/usr/bin/env python
import sys

current_path = None
current_count = 0
most_hit_path = None
most_hit_count = 0

for line in sys.stdin:
    line = line.strip()
    path, count = line.split('\t')
    
    # Convert count to int and aggregate counts for the current path
    try:
        count = int(count)
    except ValueError:
        continue

    if current_path == path:
        current_count += count
    else:
        if current_count > most_hit_count:
            most_hit_path = current_path
            most_hit_count = current_count
        
        current_path = path
        current_count = count

# Check for the last path in the loop
if current_path == path and current_count > most_hit_count:
    most_hit_path = current_path
    most_hit_count = current_count

# Emit the most hit path and its count
if most_hit_path:
    print(f"{most_hit_path}\t{most_hit_count}")

