#!/usr/bin/env python3

# Usage: kriskindle.py < input
# 
# reads from STDIN the list of candidate participants
# rules:
# two empty lines to stop reading from STDIN
# candidates must be space or punctuation delimited
# match each participant with another participant,
# with the caveat that no participant listed on the same
# line must match each other.

import sys
import re
import random

def main():
    """
    Main function to read input, process candidates, and generate matches.
    """
    # Read input from STDIN until two empty lines are encountered
    input = []
    while True:
        line = sys.stdin.readline()
        if line == '\n':
            break
        input.append(line)

    # Process input to extract candidates
    candidates = []
    for line in input:
        # Split the line into words, keeping only alphanumeric characters
        words = re.findall(r'\w+', line)
        for word in words:
            # Add each word as a candidate
            candidates.append(word)

    # Generate matches
    matches = []
    while len(candidates) > 0:
        # Randomly select a candidate
        candidate = random.choice(candidates)
        # Remove the selected candidate from the list
        candidates.remove(candidate)
        # Randomly select another candidate
        match = random.choice(candidates)
        # Remove the second candidate from the list
        candidates.remove(match)
        # Add the match to the list of matches
        matches.append((candidate, match))

    # Print the matches
    for match in matches:
        print(match[0] + ' -> ' + match[1])

if __name__ == "__main__":
    main()
