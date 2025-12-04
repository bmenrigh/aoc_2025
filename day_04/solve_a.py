#!/usr/bin/env python

import sys

fname = 'sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

grid = []
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        grid.append(list(line))

grid = list(map(list, zip(*grid))) # transpose grid so it addresses [x][y]

w = len(grid)
h = len(grid[0])


def count_neighbors(x, y):

    neigh = 0
    for xd in [-1, 0, 1]:
        nx = x + xd

        if nx < 0 or nx >= w:
            continue

        for yd in [-1, 0, 1]:
            ny = y + yd

            if y + yd < 0 or y + yd >= h:
                continue

            if xd == 0 and yd == 0:
                continue

            if grid[nx][ny] == '@':
                neigh += 1

    return neigh


access = 0
for x in range(0, w):
    for y in range(0, h):

        if grid[x][y] != '@':
            continue

        if count_neighbors(x, y) < 4:
            access += 1

print(f"Accessible roles: {access}")
