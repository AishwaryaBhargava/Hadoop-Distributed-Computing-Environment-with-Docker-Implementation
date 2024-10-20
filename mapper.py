#!/usr/bin/env python
import sys

# Function to generate n-grams from text
def generate_ngrams(text, n):
    ngrams = []
    words = text.split()  # Split text into words
    for word in words:
        for i in range(len(word) - n + 1):
            ngrams.append(word[i:i+n])
    return ngrams

# The size of the n-grams is taken from the command line argument
n = int(sys.argv[1])

# Process each line from standard input
for line in sys.stdin:
    line = line.strip()
    # Generate n-grams for the line and output them
    ngrams = generate_ngrams(line, n)
    for ngram in ngrams:
        print(f"{ngram}\t1")

