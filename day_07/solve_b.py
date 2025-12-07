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
timelines = []

start_row = [0] * w
for x in range(0, w):
    if grid[0][x] == "S":
        start_row[x] = 1

timelines.append(start_row)
for y in range(1, h):

    this_row = [0] * w
    for x in range(0, w):

        if timelines[y - 1][x] > 0:
            if grid[y][x] == ".":
                this_row[x] += timelines[y - 1][x]
            elif grid[y][x] == "^":
                splits += 1
                this_row[x - 1] += timelines[y - 1][x]
                this_row[x + 1] += timelines[y - 1][x]

    timelines.append(this_row)


print(f"Number of timelines: {sum(timelines[-1])}")
