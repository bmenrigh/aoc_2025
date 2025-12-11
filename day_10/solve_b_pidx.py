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


def solve_pidx_m(goal, buttons_p, m, u, pi, bi, c, dep_check):

    if u == m:
        if c == goal:
            return True
        else:
            return False

    if pi >= len(goal):
        return False

    if any(z[1] > z[0] for z in zip(goal, c)):
        return False

    if pi > 0 and bi == 0 and len(dep_check[pi - 1]) > 0:
        for pid in dep_check[pi - 1]:
            if c[pid] != goal[pid]:
                return False

    l = goal[pi] - c[pi]

    if len(buttons_p[pi]) == 0:
        if l != 0:
            return False
        else:
            return solve_pidx_m(goal, buttons_p, m, u, pi + 1, 0, c, dep_check)

    if m - u < l:
        return False

    nbi = bi + 1
    npi = pi

    if nbi >= len(buttons_p[pi]):
        nbi = 0
        npi += 1

        return solve_pidx_m(goal, buttons_p, m, u + l, npi, nbi, [sum(p) for p in zip(c, [l * n for n in buttons_p[pi][bi]])], dep_check)

    else:
        for i in range(l + 1):
            if solve_pidx_m(goal, buttons_p, m, u + i, npi, nbi, [sum(p) for p in zip(c, [i * n for n in buttons_p[pi][bi]])], dep_check):
                return True

        return False


def solve_min(goal_v, buttons_v):

    if sum(goal_v) == 0:
        return 0

    buttons_p = []

    #print(f"goal_v len: {len(goal_v)}")
    dep_check = []
    used_dep = set()
    used_b = set()
    for i in range(len(goal_v)):

        dep_check.append([])
        buttons_p.append([])
        for b in buttons_v:

            if not tuple(b) in used_b:
                if b[i] == 1:
                    buttons_p[i].append(b)
                    used_b.add(tuple(b))

        for j in range(i + 2, len(goal_v)):
            left = 0
            for b in buttons_v:

                if not tuple(b) in used_b:
                    if b[j] == 1:
                        left += 1

            if left == 0:
                #print(f"pidx {j} has nothing left after {i}")
                if j not in used_dep:
                    dep_check[i].append(j)
                    used_dep.add(j)

    #print(f"Dep check: {dep_check}")



    #print(buttons_p)

    m = max(sum(goal_v) // max([len(b) for b in buttons_v]), max(goal_v))
    while True:
        #print(f"Trying with m {m}")
        if solve_pidx_m(goal_v, buttons_p, m, 0, 0, 0, [0] * len(goal_v), dep_check):
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
