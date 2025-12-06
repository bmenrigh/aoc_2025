#!/usr/bin/env python

import sys
import re

spaces_re = re.compile(r'\s+')

fname = 'sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

grid = []
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        grid.append(line)


accum = []

op = ''
nlist = []
for c in range(0, max([len(r) for r in grid])):

    if c < len(grid[-1]) and grid[-1][c] in "+*":

        if op == '+':
            accum.append(0)
            for n in [int(s) for s in nlist]:
                accum[-1] += n
        elif op == '*':
            accum.append(1)
            for n in [int(s) for s in nlist]:
                accum[-1] *= n

        op = grid[-1][c]
        nlist = []

    s = ''
    for r in range(0, len(grid) - 1):

        if c < len(grid[r]) and grid[r][c] != ' ':
            s += grid[r][c]

    if s != '':
        nlist.append(s)


if op == '+':
    accum.append(0)
    for n in [int(s) for s in nlist]:
        accum[-1] += n
elif op == '*':
    accum.append(1)
    for n in [int(s) for s in nlist]:
        accum[-1] *= n


print(f"Sum of problem solutions: {sum(accum)}")
