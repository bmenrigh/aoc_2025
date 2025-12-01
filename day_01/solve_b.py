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
            a = (0 - a)

        scn = cn
        cn += a

        if cn >= 100:
            zcnt += cn // 100
        elif cn == 0:
            zcnt += 1
        elif cn < 0:
            if scn > 0:
                zcnt += 1 # we crossed zero so count it
            zcnt += ((0 - cn) // 100)

        cn %= 100

print(f"Total clicked-at-zero count: {zcnt}")
