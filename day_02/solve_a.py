#!/usr/bin/env python

import sys

fname = 'input_sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

s = 0
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        ranges = line.split(',')

        for r in ranges:
            l, h = r.split('-')

            if len(l) > 1:
                ll = int(l[:len(l) // 2]) # lower half of lower bound
            else:
                ll = 1

            if len(h) > 1:
                hl = int(h[:len(h) // 2]) # lower half of upper bound
            else:
                hl = 9

            if hl < ll:
                hl = (10 ** (len(h) // 2)) - 1

            #print(f"{l} to {h} (counting {ll} to {hl})")

            il = int(l)
            ih = int(h)
            for ch in range(ll, hl + 1):
                p = 10 ** len(str(ch))

                c = ch * p + ch

                if c >= il and c <= ih:
                    s += c
                    #print(f"invalid id: {c}")

print(f"Sum of all invalid IDs: {s}")
