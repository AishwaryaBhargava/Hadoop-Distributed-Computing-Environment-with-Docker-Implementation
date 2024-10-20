#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    line = line.strip()
    # Check if '/images/smilies/' is in the line first to improve efficiency
    if '/images/smilies/' in line:
        pattern = r'\"[A-Z]+\s(/[^ ]*)\sHTTP/1\.[01]\"'

        # Search for the pattern in the line
        try:
            match = re.search(pattern, line)
            if match:
                # Emit the path with a count of 1, using a tab character as a separator
                print(f"{match.group(1)}\t1")
        except re.error as e:
            # Log regex errors to stderr or handle them as needed
            print(f"Regex error: {e}", file=sys.stderr)

