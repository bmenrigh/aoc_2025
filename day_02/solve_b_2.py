#!/usr/bin/env python

import sys

fname = 'input_sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

s = 0

with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        invalids = {}
        ranges = line.split(',')

        for r in ranges:
            l, h = r.split('-')

            il = int(l)
            ih = int(h)

            #print(f"Got range {l} to {h}")

            for pl in range(1, (len(h) // 2) + 1):
                #print(f"Trying pattern length {pl}")
                if len(l) % pl == 0:
                    prl = len(l) // pl
                else:
                    prl = -1

                if len(h) % pl == 0:
                    pru = len(h) // pl
                else:
                    pru = -1

                if prl == -1 and pru > 0:
                    prl = pru

                if pru == -1 and prl > 0:
                    pru = prl

                if prl == 1:
                    prl = 2

                if prl == -1 or prl == -1 or prl > pru:
                    continue

                #print(f"Pattern must repeat {prl} to {pru} times")

                for p in range((10 ** (pl - 1)), 10 ** pl):
                    for pr in range(prl, pru + 1):
                        n = int(str(p) * pr)

                        if n >= il and n <= ih:
                            if not n in invalids:
                                #print(f"Invalid ID: {n}")
                                s += n
                            invalids[n] = 0




print(f"Sum of invalid IDs: {s}")
