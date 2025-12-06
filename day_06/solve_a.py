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
        l = re.split(spaces_re, line)
        if l[0] == '':
            l = l[1:]
        grid.append(l)


accum = []
for op in grid[-1]:
    if op == '+':
        accum.append(0)
    else:
        accum.append(1)

for i in range(0, len(grid[0])):
    if grid[-1][i] == '+':
        for j in range(0, len(grid) - 1):
            accum[i] += int(grid[j][i])
    else:
        for j in range(0, len(grid) - 1):
            accum[i] *= int(grid[j][i])

print(f"Sum of problem solutions: {sum(accum)}")
