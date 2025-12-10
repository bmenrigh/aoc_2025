#!/usr/bin/env python

import sys

fname = 'sample.txt'

if len(sys.argv) > 1:
    fname = sys.argv[1]


def goal_str_to_n(goal_s):

    n = 0
    p = 1
    for b in goal_s[1:len(goal_s) - 1]:
        if b == '#':
            n += p
        p *= 2

    return n


def button_str_to_n(button_s):

    n = 0
    for p in [int(ps) for ps in button_s[1:(len(button_s) - 1)].split(',')]:
        n += 2 ** p

    return n


def solve_with_m(goal, buttons, m, d, u, c):

    if d >= len(buttons) or m == u:
        if c == goal:
            return True
        else:
            return False

    if solve_with_m(goal, buttons, m, d + 1, u + 1, c ^ buttons[d]):
        return True
    if solve_with_m(goal, buttons, m, d + 1, u, c):
        return True

    return False


def solve_min(goal, buttons):

    if goal == 0:
        return 0

    for m in range(1, len(buttons) + 1):
        if solve_with_m(goal, buttons, m, 0, 0, 0):
            return m

tot = 0
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        chunks = line.split(" ")

        goal_n = goal_str_to_n(chunks[0])
        buttons = [button_str_to_n(s) for s in chunks[1:(len(chunks) - 1)]]

        #print(f"Goal {chunks[0]} as num {goal_n} using buttons {buttons}")
        c = solve_min(goal_n, buttons)
        #print(f"{c}")
        tot += c

print(f"Total minimum button presses: {tot}")
