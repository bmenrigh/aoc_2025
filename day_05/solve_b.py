#!/usr/bin/env python

import sys

fname = 'sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

ranges = {}
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        if line == '':
            break

        l, u = [int(n) for n in line.split('-')]

        if not l in ranges:
            ranges[l] = u
        else:
            if u > ranges[l]:
                ranges[l] = u

#for l, u in ranges.items():
#    print(f"Got range {l}-{u}")

#for i in ingred:
#    print(f"Got ingredient {i}")

# merge overlapping ranges
prev_l, prev_u = -1, -1

for l in sorted(ranges.keys()):
    u = ranges[l]

    if prev_l < l <= prev_u:
        if prev_u < u:
            ranges[prev_l] = u
            prev_u = u

        del ranges[l]
    else:
        prev_l, prev_u = l, u

span = 0
for l in ranges.keys():
    span += (ranges[l] - l) + 1

print(f"Total good IDs: {span}")

