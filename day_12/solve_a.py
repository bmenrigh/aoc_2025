#!/usr/bin/env python

import sys

fname = 'sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

pieces = []
pgrids = []

plines = []
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:

        if len(line) == 0:
            if len(plines) > 0:
                piece = [list(l) for l in plines]
                print(f"Got piece: {piece}")
                pieces.append(piece)
                plines = []
            continue

        if len(line) == 2 and line[1] == ':':
            continue

        if len(line) == 3:
            plines.append(line)
            continue

        if len(line) < 10:
            print(f"BUG: line len {len(line)} not expected for line {line}")
            exit(-1)

        w, h = int(line[:line.index("x")]), int(line[line.index("x") + 1:line.index(":")])

        pcounts = [int(c) for c in line[line.index(" ") + 1:].split(" ")]

        pgrid = [[w, h], pcounts]
        pgrids.append(pgrid)

        print(f"Got puzzle grid {w}x{h} with piece counts {pcounts}")

psize = []
for p in pieces:
    pcnt = 0
    for r in p:
        for c in r:
            if c == "#":
                pcnt += 1

    psize.append(pcnt)

print(f"Piece sizes: {psize}")

imp = 0
maybe = 0
trivial = 0
for pg in pgrids:

    pg_area = pg[0][0] * pg[0][1]
    pg_need = sum([z[0] * z[1] for z in zip(psize, pg[1])])
    pg_area_9 = (pg[0][0] - (pg[0][0] % 3)) * (pg[0][1] - (pg[0][1] % 3))
    pg_need_9 = sum([9 * z[1] for z in zip(psize, pg[1])])

    if pg_need_9 < pg_area_9:
        trivial += 1
        print(f"Trivial: area: {pg_area_9}, needed: {pg_need_9}, puzzle: {pg}")
    elif pg_need < pg_area:
        print(f"Maybe possible: area: {pg_area}, needed: {pg_need}, max needed {pg_need_9}, puzzle: {pg}")
        maybe += 1
    else:
        imp += 1
        print(f"Impossible: area: {pg_area}, needed: {pg_need}, puzzle: {pg}")



print(f"Impossible count: {imp}, maybe count: {maybe}, trivial count: {trivial}")

