#!/usr/bin/env python

import sys

fname = 'sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

s = 0
dig = 12

with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:

        dlist = ['-'] * dig

        ci = 0 # current starting search index
        ll = len(line)
        for d in range(0, dig):
            e = (ll - dig) + d + 1
            #print(f"searching {ci} to {e}: {line[ci:e]}")
            dm = max(line[ci:e])
            dmi = line[ci:e].index(dm)

            dlist[d] = dm
            ci += dmi + 1



        j = int(''.join(dlist))

        #print(f"Bank {line} has max jolts {j}")

        s += j


print(f"Sum of bank joltss: {s}")
