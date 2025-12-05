#!/usr/bin/env python

import sys

fname = 'sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

ranges = {}
ingred = []
inranges = True
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        if line == '':
            inranges = False
            continue

        if inranges:
            l, u = [int(n) for n in line.split('-')]

            if not l in ranges:
                ranges[l] = u
            else:
                if u > ranges[l]:
                    ranges[l] = u

            continue

        if not inranges:
            ingred.append(int(line))

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


#for l, u in ranges.items():
#    print(f"New range {l}-{u}")

l_list = sorted(ranges.keys())

def n_in_ranges(n, ll, r):
    ll_len = len(ll)

    if n < ll[0]:
        return False

    if n > ll[-1]:
        if n <= ranges[ll[-1]]:
            return True
        else:
            return False

    i = ll_len // 2
    il, iu = 0, ll_len - 2
    while not ll[i] <= n < ll[i + 1]:
        if n < ll[i]:
            iu = i - 1
        else:
            il = i + 1

        i = (il + iu) // 2
    else:
        #print(f"For {n} found candidate range {ll[i]}-{r[ll[i]]}")
        if n <= r[ll[i]]:
            #print(f"{n} is good")
            return True
        else:
            #print(f"{n} is bad")
            return False

good = 0
for n in ingred:
    if n_in_ranges(n, l_list, ranges):
        good += 1

print(f"Good ingredients: {good}")
