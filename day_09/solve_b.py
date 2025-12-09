#!/usr/bin/env python

import sys
import math

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

        points.append(tuple(p))

for x in x_to_y.keys():
    x_to_y[x] = sorted(x_to_y[x])

for y in y_to_x.keys():
    y_to_x[y] = sorted(y_to_x[y])

x_sort = sorted(x_to_y.keys())
y_sort = sorted(y_to_x.keys())

lines_v = {}
lines_h = {}

pp = points[-1]
for cp in points:
    if cp[0] == pp[0]:
        # vertical line
        if not cp[0] in lines_v:
            lines_v[cp[0]] = []

        if pp[1] < cp[1]:
            t = (pp[1], cp[1])
        else:
            t = (cp[1], pp[1])

        lines_v[cp[0]].append(t)
    else:
        # horizontal line
        if not cp[1] in lines_h:
            lines_h[cp[1]] = []

        if pp[0] < cp[0]:
            t = (pp[0], cp[0])
        else:
            t = (cp[0], pp[0])

        lines_h[cp[1]].append(t)

    pp = cp

#print(lines_v)

def check_box(x_l, x_r, y_t, y_b):

    #a = ((y_t - y_b) + 1) * ((x_r - x_l) + 1)

    #print(f"Checking box {x_l}, {x_r}, {y_t}, {y_b} with area {a}")

    # vertical lines crossing top or bottom of box
    for vx in [x for x in lines_v.keys() if x > x_l and x < x_r]:
        for (v_l, v_u) in lines_v[vx]:
            # top
            #print(f"v-line from {v_l} to {v_u} against top at {y_t} and bottom at {y_b}")
            if v_l < y_t and v_u >= y_t:
                return False
            # bottom
            if v_u > y_b and v_l <= y_b:
                return False

    for hy in [y for y in lines_h.keys() if y > y_b and y < y_t]:
        for (h_l, h_u) in lines_h[hy]:
            # left
            if h_u > x_l and h_l <= x_l:
                return False

            # right
            if h_l < x_r and h_u >= x_r:
                return False

    return True

def find_hlines(x_l, x_r):

    hlines_y = []
    for hy in reversed(y_sort):
        for (h_l, h_u) in lines_h[hy]:
            # left
            if h_u > x_l and h_l <= x_l:
                hlines_y.append(hy)
                continue

            # right
            if h_l < x_r and h_u >= x_r:
                hlines_y.append(hy)
                continue

    return hlines_y

area = 0
for x_l in x_sort:
    for x_r in reversed(x_sort):
        if x_l > x_r:
            break

        #hlines_y = find_hlines(x_l, x_r)

        xd = (x_r - x_l) + 1

        # \ direction
        for y_t in reversed(x_to_y[x_l]):

            #min_y = 0
            #for hl_y in hlines_y:
            #    if hl_y < y_t:
            #        min_y = hl_y
            #        break

            for y_b in x_to_y[x_r]:
                #if y_b < min_y:
                #    continue

                if y_b <= y_t:

                    yd = (y_t - y_b) + 1

                    na = xd * yd
                    if na > area and check_box(x_l, x_r, y_t, y_b):
                        #print(f"Found area \\ {na} from {x_l},{y_t} and {x_r},{y_b}")
                        area = na

                else:
                   break

        # / direction
        for y_t in reversed(x_to_y[x_r]):

            #min_y = 0
            #for hl_y in hlines_y:
            #    if hl_y < y_t:
            #        min_y = hl_y
            #        break

            for y_b in x_to_y[x_l]:
                #if y_b < min_y:
                #    continue

                if y_b <= y_t:

                    yd = (y_t - y_b) + 1

                    na = xd * yd
                    if na > area and check_box(x_l, x_r, y_t, y_b):
                        #print(f"Found area / {na} from {x_l},{y_b} and {x_r},{y_t}")
                        area = na

                else:
                    break

print(f"Largest area found: {area}")
