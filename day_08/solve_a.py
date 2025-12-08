#!/usr/bin/env python

import sys

fname = 'sample.txt'

cons = 10

if len(sys.argv) > 1:
    fname = sys.argv[1]

if len(sys.argv) > 2:
    cons = int(sys.argv[2])

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

#print(pair_dist.items())
con_lists = {}
for d in [d for d in sorted(pair_dist.items(), key=lambda i: i[1]) if d[1] > 0][:cons]:
    p1 = (d[0][0], d[0][1], d[0][2])
    p2 = (d[0][3], d[0][4], d[0][5])

    #print(f"Connecting {p1} to {p2}")

    if not p1 in con_lists:
        con_lists[p1] = []
    con_lists[p1].append(p2)

    if not p2 in con_lists:
        con_lists[p2] = []
    con_lists[p2].append(p1)


def group_size(pairs, p, mem):

    if p in mem:
        return 0

    mem[p] = 1
    cnt = 1

    for p2 in pairs[p]:
        cnt += group_size(pairs, p2, mem)

    return cnt

mem = {}
gs = []
for p in con_lists:
    if not p in mem:
        gs.append(group_size(con_lists, p, mem))

gs = sorted(gs)
print(f"Most connected group sizes {gs[-3:]} product: {gs[-1] * gs[-2] * gs[-3]}")
