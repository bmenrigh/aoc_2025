#!/usr/bin/env python

import sys

fname = 'sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

grid = []
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        grid.append(list(line))

w = len(grid[0])
h = len(grid)

splits = 0

for y in range(1, h):
    for x in range(0, w):

        if grid[y - 1][x] in "S|":
            if grid[y][x] == ".":
                grid[y][x] = "|"
            elif grid[y][x] == "^":
                splits += 1
                grid[y][x - 1] = "|"
                grid[y][x + 1] = "|"

print(f"Number of splits: {splits}")
