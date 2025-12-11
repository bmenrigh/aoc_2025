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

def solve_f_with_m(goal, buttons_i, m, d, u, c, mem):

    if d >= len(buttons_i) or m == u:
        mem.add(tuple(c))
        if c == goal:
            return True
        else:
            return False

    if any([z[1] > z[0] for z in zip(goal, c)]):
        return False

    if solve_f_with_m(goal, buttons_i, m, d + 1, u, c, mem):
        return True

    s = 1
    if d == len(buttons_i) - 1:
        s = (m - u)

    for i in range(s, (m - u) + 1):
        if solve_f_with_m(goal, buttons_i, m, d + 1, u + i, [sum(p) for p in zip(c, buttons_i[d][i - 1])], mem):
            return True


    return False

def add_layer_f(goal, buttons_v, p_mem, mem):

    for c in p_mem:
        for b in buttons_v:
            nc = tuple([sum(p) for p in zip(c, b)])

            if not any([z[1] > z[0] for z in zip(goal, nc)]):
                mem.add(nc)

def add_layer_b(goal, buttons_v, p_mem, mem):

    for c in p_mem:
        for b in buttons_v:
            nc = tuple([p[0] - p[1] for p in zip(c, b)])

            if not any([z < 0 for z in nc]):
                mem.add(nc)


def solve_b_with_m(goal, buttons_i, m, d, u, c, mem):

    if d >= len(buttons_i) or m == u:
        mem.add(tuple(c))
        if c == goal:
            return True
        else:
            return False

    if any([z < 0 for z in c]):
        return False

    if solve_b_with_m(goal, buttons_i, m, d + 1, u, c, mem):
        return True

    s = 1
    if d == len(buttons_i) - 1:
        s = (m - u)

    for i in range(s, (m - u) + 1):
        if solve_b_with_m(goal, buttons_i, m, d + 1, u + i, [p[0] - p[1] for p in zip(c, buttons_i[d][i - 1])], mem):
            return True


    return False


def solve_min_mitm(goal_v, buttons_v):

    if sum(goal_v) == 0:
        return 0

    buttons_i = []
    for bi in range(len(buttons_v)):
        buttons_i.append([])
        for i in range(1, 250):
            buttons_i[bi].append([i * n for n in buttons_v[bi]])

    m = sum(goal_v) // max([len(b) for b in buttons_v])
    f_m = m // 2
    b_m = m // 2

    f_mem_p = set()
    b_mem_p = set()
    while True:

        if len(f_mem_p) == 0:
            f_mem = set()
            solve_f_with_m(goal_v, buttons_i, f_m, 0, 0, [0] * len(goal_v), f_mem)
        else:
            f_mem = set()
            add_layer_f(goal_v, buttons_v, f_mem_p, f_mem)

        if len(f_mem & b_mem_p):
            return f_m + (b_m - 1)

        if len(b_mem_p) == 0:
            b_mem = set()
            solve_b_with_m([0] * len(goal_v), buttons_i, b_m, 0, 0, goal_v, b_mem)
        else:
            b_mem = set()
            add_layer_b(goal_v, buttons_v, b_mem_p, b_mem)

        if len(f_mem & b_mem):
            return f_m + b_m

        f_m += 1
        b_m += 1
        f_mem_p = f_mem
        b_mem_p = b_mem

tot = 0
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        chunks = line.split(" ")

        goal_v = str_to_l(chunks[-1])

        buttons_v = [button_l_to_v(str_to_l(s), len(goal_v)) for s in chunks[1:(len(chunks) - 1)]]

        #if len(goal_v) != len(buttons_v):
        #    print(goal_v)
        #    print(buttons_v)

        c = solve_min_mitm(goal_v, buttons_v)
        print(f"{c}")
        tot += c

print(f"Total minimum button presses: {tot}")
