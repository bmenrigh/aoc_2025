#!/usr/bin/env python

import sys

fname = 'sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

points = []
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        p = tuple([int(c) for c in line.split(",")])
        points.append(p)

pair_dist = {}
p_cnt = len(points)
for pn1 in range(p_cnt):
    for pn2 in range(pn1):

        p1 = points[pn1]
        p2 = points[pn2]
        pair_dist[p1 + p2] = ((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2) + ((p2[2] - p1[2]) ** 2)


gn = 0
p_to_g = {}
g_to_p = {}

for d in [d for d in sorted(pair_dist.items(), key=lambda i: i[1]) if d[1] > 0]:
    p1 = (d[0][0], d[0][1], d[0][2])
    p2 = (d[0][3], d[0][4], d[0][5])

    # if p1 not seen yet swap it to second
    if not p1 in p_to_g:
        p1, p2 = p2, p1

    if p1 in p_to_g:
        p1g = p_to_g[p1]

        if p2 in p_to_g:
            p2g = p_to_g[p2]

            # Need to merge groups
            if p1g != p2g:

                # Swap the groups to make g2 the smaller
                if len(g_to_p[p1g]) < len(g_to_p[p2g]):
                    p1, p2 = p2, p1
                    p1g, p2g = p2g, p1g

                for p in g_to_p[p2g]:
                    p_to_g[p] = p1g

                g_to_p[p1g] = g_to_p[p1g] + g_to_p[p2g]
                del g_to_p[p2g]

        else:
            # put p2 in g1
            p_to_g[p2] = p1g
            g_to_p[p1g].append(p2)

    else:
        # make a new group:
        p_to_g[p1] = gn
        p_to_g[p2] = gn

        g_to_p[gn] = [p1, p2]

        gn += 1

    # Check if this was the last connection needed:
    if len(g_to_p) == 1:
        if len(p_to_g) == p_cnt:
            print(f"Last pair connection: {p1} to {p2}, x-prod: {p1[0] * p2[0]}")
            break
