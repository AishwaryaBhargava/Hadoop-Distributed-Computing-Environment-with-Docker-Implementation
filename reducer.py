#!/usr/bin/env python
import sys

current_ngram = None
current_count = 0
ngram = None

for line in sys.stdin:
    line = line.strip()
    ngram, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_ngram == ngram:
        current_count += count
    else:
        if current_ngram:
            # Updated line using the format method for compatibility
            print('{}\t{}'.format(current_ngram, current_count))
        current_count = count
        current_ngram = ngram

if current_ngram == ngram:
    # Updated line using the format method for compatibility
    print('{}\t{}'.format(current_ngram, current_count))

