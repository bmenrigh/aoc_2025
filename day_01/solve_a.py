#!/usr/bin/env python

import sys

fname = 'input_sample_a.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

cn = 50  # current number starts at 50
zcnt = 0 # pointing at zero count
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        # Example line: L68
        d = line[0]       # direction
        a = int(line[1:]) # amount

        # Left is towards lower numbers
        if d == 'L':
            a *= -1

        cn = (cn + a) % 100

        if cn == 0:
            zcnt += 1

print(f"Total pointing-at-zero count: {zcnt}")
