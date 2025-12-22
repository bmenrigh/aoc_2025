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
    rows = len(g_v)
    b_v.append(g_v)

    b_m = list(map(list, zip(*b_v))) # transpose to column matrix

    rm = reduce_m(b_m)

    free_c = []
    dep_c = set()

    r_to_fc = [-1] * rows

    pc = 0
    for r in range(rows):
        fc = -1
        for nc in range(pc, bn):
            if rm[r][nc] != 0:
                pc = nc
                fc = nc
                r_to_fc[r] = fc
                break

        if fc < 0:
            #print(f"No first column found for row {r}")
            continue

        dep_c.add(fc)

    for c in range(bn):
        if not c in dep_c:
            free_c.append(c)

    #print(f"Free columns: {free_c}")
    fcn = len(free_c)

    if fcn == 0:
        return sum([rm[r][bn] for r in range(rows)])

    min_c = sum(goal_v)

    def try_combo(d, l, gc):

        nonlocal min_c

        if d >= fcn:

            coef = [0] * bn
            for i, x in enumerate(l):
                coef[free_c[i]] = x

            #print(f"Finding solution with free column selection {l} ({coef})")

            for r in range(rows):

                if r_to_fc[r] < 0:
                    continue # blank row

                x = rm[r][bn]

                for i in free_c:
                    x -= rm[r][i] * coef[i]

                if x < 0:
                    #print(f"Computed x for row {r} was negative ({x})")
                    return

                if x % rm[r][r_to_fc[r]] != 0:
                    #print(f"Computed x for row {r} wasn't an int ({x}/{fc})")
                    return

                coef[r_to_fc[r]] = x // rm[r][r_to_fc[r]]

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
        ub = min([g for i, g in enumerate(gc) if b_v[free_c[d]][i] == 1])

        #print(f"UB for depth {d} is {ub}, previous selections {l} with gc {gc}")

        for i in range(ub + 1):
            try_combo(d + 1, l + [i], [g - b_v[free_c[d]][j] * i for j, g in enumerate(gc)])


    gc = g_v.copy()

    # Any dependent row that doesn't depend on a free column is determined
    for r in range(rows):
        if r_to_fc[r] < 0:
            continue

        if all([rm[r][c] == 0 for c in free_c]):
            if rm[r][bn] % rm[r][r_to_fc[r]] != 0:
                print(f"Bug? Fractional determined row {rm[r]}")
                continue

            x = rm[r][bn] // rm[r][r_to_fc[r]]

            gc = [g - b_v[r_to_fc[r]][j] * x for j, g in enumerate(gc)]
            #print(f"Row {r} able to reduce gc to {gc}")

    try_combo(0, [], gc)

    return min_c

tot = 0
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        chunks = line.split(" ")

        goal_v = str_to_l(chunks[-1])

        buttons_v = [button_l_to_v(str_to_l(s), len(goal_v)) for s in chunks[1:(len(chunks) - 1)]]

        m = solve_min(buttons_v, goal_v)
        #print(f"{m}")
        tot += m

print(f"Got total button presses: {tot}")

