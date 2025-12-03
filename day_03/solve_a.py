#!/usr/bin/env python

import sys

fname = 'sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

s = 0

with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        fm = max(line[:-1])
        fmi = line.index(fm)

        sm = max(line[fmi + 1:])

        j = int(fm + sm)

        #print(f"Bank {line} has max jolts {j}")

        s += j


print(f"Sum of bank joltss: {s}")
