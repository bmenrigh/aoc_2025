#!/usr/bin/env python

import sys

fname = 'sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

if len(sys.argv) > 2:
    cons = int(sys.argv[2])

points = []
x_to_y = {}
y_to_x = {}
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        p = [int(c) for c in line.split(",")]

        if not p[0] in x_to_y:
            x_to_y[p[0]] = []

        x_to_y[p[0]].append(p[1])

        if not p[1] in y_to_x:
            y_to_x[p[1]] = []

        y_to_x[p[1]].append(p[0])

for x in x_to_y.keys():
    x_to_y[x] = sorted(x_to_y[x])

for y in y_to_x.keys():
    y_to_x[y] = sorted(y_to_x[y])


x_sort = sorted(x_to_y.keys())
y_sort = sorted(y_to_x.keys())


area = 0
for x_r in x_sort:
    for x_l in reversed(x_sort):
        if x_r > x_l:
            break

        xd = (x_l - x_r) + 1

        # \ direction
        y_b = x_to_y[x_r][0]
        y_t = x_to_y[x_l][-1]
        if y_b <= y_t:

            yd = (y_t - y_b) + 1

            na = xd * yd
            if na > area:
                area = na

        # / direction
        y_b = x_to_y[x_l][0]
        y_t = x_to_y[x_r][-1]
        if y_b <= y_t:

            yd = (y_t - y_b) + 1

            na = xd * yd
            if na > area:
                area = na

print(f"Largest area found: {area}")
