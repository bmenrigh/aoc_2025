#!/usr/bin/env python

import sys

fname = 'sample_b.txt'

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


def count_from_node(n, g, mem):
    if n in mem:
        return mem[n]

    if n == "out" and g != "out":
        return 0

    if n == g:
        return 1

    s = 0
    for nn in nodes[n]:
        s += count_from_node(nn, g, mem)

    mem[n] = s
    return s


paths = count_from_node("svr", "fft", dict()) * count_from_node("fft", "dac", dict()) * count_from_node("dac", "out", dict())

print(f"Paths from svr to out via fft then dac: {paths}")
