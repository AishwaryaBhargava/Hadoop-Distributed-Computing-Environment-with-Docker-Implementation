import sys
import re

for line in sys.stdin:
    line = line.strip()
    # Look for lines that contain the "POST" method
    if "POST " in line:
        print(f'POST\t1')

