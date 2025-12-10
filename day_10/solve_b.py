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

def solve_with_m(goal, buttons, m, d, u, c):

    if d >= len(buttons) or m == u:
        if c == goal:
            return True
        else:
            return False

    if any([z[1] > z[0] for z in zip(goal, c)]):
        return False

    if solve_with_m(goal, buttons, m, d + 1, u, c):
        return True

    for i in range(1, (m - u) + 1):
        if solve_with_m(goal, buttons, m, d + 1, u + i, [sum(p) for p in zip(c, [i * n for n in buttons[d]])]):
            return True


    return False


def solve_min(goal_v, buttons_v):

    if sum(goal_v) == 0:
        return 0

    m = max(goal_v)
    while True:
        if solve_with_m(goal_v, buttons_v, m, 0, 0, [0] * len(goal_v)):
            return m

        m += 1

tot = 0
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        chunks = line.split(" ")

        goal_v = str_to_l(chunks[-1])

        buttons_v = [button_l_to_v(str_to_l(s), len(goal_v)) for s in chunks[1:(len(chunks) - 1)]]

        if len(goal_v) != len(buttons_v):
            print(goal_v)
            print(buttons_v)

        #c = solve_min(goal_v, buttons_v)
        #print(f"{c}")
        #tot += c

print(f"Total minimum button presses: {tot}")
