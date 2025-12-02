#!/usr/bin/env python

import sys
import re

# My effecient solution for part a is much more work to do in this case...
# Regular expressions would make the task trivial :-(

pattern_re = re.compile(r'^([0-9]+)\1+$')

fname = 'input_sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

s = 0
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        ranges = line.split(',')

        for r in ranges:
            l, h = r.split('-')

            il = int(l)
            ih = int(h)
            for n in range(il, ih + 1):
                if re.match(pattern_re, str(n)):
                    #print(f"Invalid ID: {n}")
                    s += n

print(f"Sum of invalid IDs: {s}")
