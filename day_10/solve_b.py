#!/usr/bin/env python

import sys

fname = 'sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]

def str_to_l(s):

    return [int(n) for n in s[1:len(s) - 1].split(",")]

def button_l_to_v(l, n):
    v = [0] * n

    for i in l:
        v[i] = 1

    return v

def solve_with_m(goal, buttons_i, m, d, u, c):

    if d >= len(buttons_i) or m == u:
        if c == goal:
            return True
        else:
            return False

    if any([z[1] > z[0] for z in zip(goal, c)]):
        return False

    if solve_with_m(goal, buttons_i, m, d + 1, u, c):
        return True

    s = 1
    if d == len(buttons_i) - 1:
        s = (m - u)

    for i in range(s, (m - u) + 1):
        if solve_with_m(goal, buttons_i, m, d + 1, u + i, [sum(p) for p in zip(c, buttons_i[d][i - 1])]):
            return True


    return False


def solve_min(goal_v, buttons_v):

    if sum(goal_v) == 0:
        return 0

    buttons_i = []
    for bi in range(len(buttons_v)):
        buttons_i.append([])
        for i in range(1, 250):
            buttons_i[bi].append([i * n for n in buttons_v[bi]])

    m = sum(goal_v) // max([len(b) for b in buttons_v])
    while True:
        if solve_with_m(goal_v, buttons_i, m, 0, 0, [0] * len(goal_v)):
            return m

        m += 1

tot = 0
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        chunks = line.split(" ")

        goal_v = str_to_l(chunks[-1])

        buttons_v = [button_l_to_v(str_to_l(s), len(goal_v)) for s in chunks[1:(len(chunks) - 1)]]

        #if len(goal_v) != len(buttons_v):
        #    print(goal_v)
        #    print(buttons_v)

        c = solve_min(goal_v, buttons_v)
        print(f"{c}")
        tot += c

print(f"Total minimum button presses: {tot}")
