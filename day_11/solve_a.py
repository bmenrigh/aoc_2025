#!/usr/bin/env python

import sys

fname = 'sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

nodes = {}
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        nl = line.split(' ')

        s = nl[0][:len(nl[0]) - 1]

        if s in nodes:
            print(f"Bug: already saw node {s}")
            exit(-1)

        nodes[s] = nl[1:]


def count_from_node(n, mem):
    if n in mem:
        return mem[n]

    if n == "out":
        return 1

    s = 0
    for nn in nodes[n]:
        s += count_from_node(nn, mem)

    mem[n] = s
    return s


paths = count_from_node("you", dict())

print(f"Paths from you to out: {paths}")
