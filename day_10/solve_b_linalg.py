#!/usr/bin/env python

import sys
import math
import copy

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


def gcd_l(l):
    g = l[0]
    for i in range(1, len(l)):
        g = math.gcd(g, l[i])

    return g


def m_str(m):

    s = "\n"

    for r in m:
        for c in r:
            s += f"{c:4}"

        s += "\n"

    return s


def reduce_m(m):

    rm = copy.deepcopy(m)

    w = len(rm[0])
    h = len(rm)

    #print(f"Reducing {w}x{h} matrix {m_str(rm)}")

    for c in range(w - 1):
        #print(f"Working on column {c}")
        # Find a row whose leading term is this column
        for r in range(c, h):
            if all([rm[r][i] == 0 for i in range(0, c)]) and rm[r][c] != 0:
                #print(f"Found row {r} with {c} leading zeros: {rm[r]}")
                if r != c:
                    #print(f"Swapping rows {c} and {r}")

                    rm[c], rm[r] = rm[r], rm[c]
                break

        if c >= h:
            continue

        fc = -1
        for nc in range(w - 1):
            if rm[c][nc] != 0:
                fc = nc
                break

        if fc < 0:
            continue

        #print(f"Checking row {c} with first col {fc} {rm[c]} for elmination of other rows")

        for r in range(0, h):
            if r == c:
                continue

            if rm[r][fc] == 0:
                continue

            cm = math.lcm(rm[r][fc], rm[c][fc])
            a = cm // rm[r][fc]
            b = cm // rm[c][fc]

            #print(f"Subtracting {b} copies of row {c} from {a} copies of row {r}")

            for nc in range(0, w):
                rm[r][nc] = a * rm[r][nc] - b * rm[c][nc]

    # Factor constants out of rows as much as possible
    for r in range(h):

        g = gcd_l(rm[r])

        if g == 0:
            continue

        nf = 1 # negative factor
        for c in range(w):
            if rm[r][c] != 0:
                if rm[r][c] < 0:
                    nf = -1
                break

        g *= nf

        for c in range(w):
            rm[r][c] //= g

    #print(f"Reduced matrix: {m_str(rm)}")

    return rm


def solve_min(b_v, g_v):

    bn = len(b_v)
    b_v.append(g_v)

    b_m = list(map(list, zip(*b_v))) # transpose to column matrix

    rm = reduce_m(b_m)

    free_c = []
    for c in range(bn):
        if c >= len(g_v) or rm[c][c] == 0:
            free_c.append(c)

    #print(f"Free columns: {free_c}")
    fcn = len(free_c)

    #ub = [] # upper bound of free columns
    #for fc in free_c:
    #    ub.append(min([g for i, g in enumerate(g_v) if b_v[fc][i] == 1]))

    #print(f"Upper bounds on free cols: {ub}")

    min_c = sum(goal_v)

    def try_combo(d, l, gc):

        nonlocal min_c

        if d >= fcn:

            coef = [0] * bn
            for i, x in enumerate(l):
                coef[free_c[i]] = x

            #print(f"Finding solution with free column selection {l} ({coef})")

            rt = min(bn, len(g_v))
            for r in range(rt):

                if rm[r][r] == 0:
                    continue # free column

                x = rm[r][bn]

                for i in range(bn):
                    x -= rm[r][i] * coef[i]

                if x < 0:
                    return

                if x % rm[r][r] != 0:
                    return

                coef[r] = x // rm[r][r]

            t_v = [0] * len(g_v)
            for i in range(bn):
                for j in range(len(g_v)):
                    if b_v[i][j] == 1:
                        t_v[j] += coef[i]

            if t_v != g_v:
                #print(f"Got bogus goal {t_v} for coef {coef}, expected {g_v}")
                return
            #else:
                #print(f"Got valid solution {t_v} for coef {coef}")

            s = sum(coef)
            if s < min_c:
                min_c = s
                #print(f"New minimal solution {s} with coef {coef}")

            return

        # Compute an ubber bound for how many times we could press this button
        ub = min([g for i, g in enumerate(gc) if b_v[d][i] == 1])

        for i in range(ub + 1):
            try_combo(d + 1, l + [i], [g - b_v[d][j] * i for j, g in enumerate(gc)])

    try_combo(0, [], g_v)

    return min_c

tot = 0
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        chunks = line.split(" ")

        goal_v = str_to_l(chunks[-1])

        buttons_v = [button_l_to_v(str_to_l(s), len(goal_v)) for s in chunks[1:(len(chunks) - 1)]]

        m = solve_min(buttons_v, goal_v)
        print(f"{m}")
        tot += m

print(f"Got total button presses: {tot}")

