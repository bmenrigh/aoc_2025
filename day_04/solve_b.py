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

ngrid = [] # A neighbor count grid
for i in range(w):
    ngrid.append([-1] * h)

def count_neighbors(x, y, g):

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

            if g[nx][ny] == '@':
                neigh += 1

    return neigh


def dec_neighbors(x, y, g):

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

            g[nx][ny] -= 1


access = 0
for x in range(0, w):
    for y in range(0, h):

        if grid[x][y] != '@':
            continue

        ngrid[x][y] = count_neighbors(x, y, grid)


def try_rem(x, y, g):

    rem = 0
    if 0 <= g[x][y] < 4:
        g[x][y] = -1
        rem += 1
        dec_neighbors(x, y, g)

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

                rem += try_rem(nx, ny, g)

    return rem

rem_count = 0
for x in range(0, w):
    for y in range(0, h):

        rem_count += try_rem(x, y, ngrid)


print(f"Accessible roles: {rem_count}")
