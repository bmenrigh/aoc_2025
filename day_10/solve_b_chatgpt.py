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


from fractions import Fraction
from itertools import product

def solve_min(goal_v, basis_v):
    """
    Solve:
        minimize sum_i x_i
        subject to sum_i x_i * basis_v[i][j] = goal_v[j] for all j
                  x_i >= 0, integer

    goal_v: list of length d (target vector)
    basis_v: list of n basis vectors, each a list of length d

    Returns:
        (coeffs, total_uses)  where coeffs[i] is how many times to use basis_v[i]
        or None if no non-negative integer solution exists.
    """
    d = len(goal_v)
    n = len(basis_v)

    if n == 0:
        raise ValueError("basis_v must contain at least one vector.")

    # Basic shape checks
    for i, v in enumerate(basis_v):
        if len(v) != d:
            raise ValueError("basis_v[{}] has length {}, but goal_v has length {}"
                             .format(i, len(v), d))

    # Build augmented matrix M (d rows, n+1 columns): [A | g]
    # A has columns = basis vectors
    M = []
    for row in range(d):
        # row j collects basis_v[i][j] for all i
        mat_row = [Fraction(basis_v[col][row]) for col in range(n)]
        mat_row.append(Fraction(goal_v[row]))
        M.append(mat_row)

    # Gaussian elimination to RREF
    row = 0
    pivots = []  # list of pivot column indices
    for col in range(n):
        if row >= d:
            break
        # Find pivot row with non-zero in this column
        pivot_row = None
        for r in range(row, d):
            if M[r][col] != 0:
                pivot_row = r
                break
        if pivot_row is None:
            continue

        # Swap pivot row into place
        if pivot_row != row:
            M[row], M[pivot_row] = M[pivot_row], M[row]

        # Normalize pivot row to make leading entry = 1
        pivot_val = M[row][col]
        if pivot_val != 1:
            for k in range(col, n + 1):
                M[row][k] /= pivot_val

        # Eliminate this column from all other rows
        for r in range(d):
            if r == row:
                continue
            factor = M[r][col]
            if factor != 0:
                for k in range(col, n + 1):
                    M[r][k] -= factor * M[row][k]

        pivots.append(col)
        row += 1

    # Check for inconsistency: [0 0 ... 0 | nonzero]
    for r in range(d):
        if all(M[r][c] == 0 for c in range(n)) and M[r][n] != 0:
            return None  # No solution

    # Identify free columns
    pivot_set = set(pivots)
    free_cols = [c for c in range(n) if c not in pivot_set]
    k = len(free_cols)  # number of free variables

    # Map pivot column -> pivot row index
    pivot_row_for_col = {}
    for r, c in enumerate(pivots):
        pivot_row_for_col[c] = r

    # We want: x_i = C[i] + sum_s B[i][s] * y_s
    # where y_s are the free variables (one per free column).
    C = [Fraction(0) for _ in range(n)]
    B = [[Fraction(0) for _ in range(k)] for _ in range(n)]

    # Free variables: x_free = y_s
    for s, col in enumerate(free_cols):
        C[col] = Fraction(0)
        B[col][s] = Fraction(1)

    # Pivot variables: x_pivot = RHS - sum_f (coeff * x_free)
    for col in pivots:
        r = pivot_row_for_col[col]
        C[col] = M[r][n]
        for s, fcol in enumerate(free_cols):
            coeff = M[r][fcol]
            if coeff != 0:
                B[col][s] = -coeff

    # Compute simple upper bounds for each coefficient x_i
    # For each basis vector i, x_i <= min goal_j over j where basis_v[i][j] == 1.
    # If a basis vector is all zeros, it can never help meet the goal, so its
    # optimal coefficient is 0; we set U_i = 0 for it.
    U = []
    for i in range(n):
        ones_positions = [j for j, val in enumerate(basis_v[i]) if val != 0]
        if not ones_positions:
            U.append(0)
        else:
            U.append(min(goal_v[j] for j in ones_positions))

    # If there are no free variables, we have a unique solution
    if k == 0:
        x = []
        for i in range(n):
            val = C[i]
            if val.denominator != 1 or val < 0:
                return None
            if val > U[i]:
                # Can't exceed coordinate-based bound
                return None
            x.append(int(val))

        # Optional: verify A x = g
        for j in range(d):
            s = 0
            for i in range(n):
                s += x[i] * basis_v[i][j]
            if s != goal_v[j]:
                return None

        return x, sum(x)

    # Otherwise, brute-force over the free variables y_s,
    # each in range [0, U[free_cols[s]]].
    ranges = []
    for s, col in enumerate(free_cols):
        max_val = U[col]
        if max_val < 0:
            # Impossible for that variable to be non-negative and satisfy bounds
            return None
        ranges.append(range(0, max_val + 1))

    best_sum = None
    best_x = None

    for y_tuple in product(*ranges):
        # Compute x from y
        x = []
        ok = True
        for i in range(n):
            val = C[i]
            # val += sum_s B[i][s] * y_s
            for s in range(k):
                if B[i][s] != 0 and y_tuple[s] != 0:
                    val += B[i][s] * y_tuple[s]

            # Must be integer, >= 0, and respect the simple upper bound
            if val < 0 or val.denominator != 1 or val > U[i]:
                ok = False
                break

            x.append(int(val))

        if not ok:
            continue

        # Verify A x = g exactly
        for j in range(d):
            s = 0
            for i in range(n):
                s += x[i] * basis_v[i][j]
            if s != goal_v[j]:
                ok = False
                break

        if not ok:
            continue

        total = sum(x)
        if best_sum is None or total < best_sum:
            best_sum = total
            best_x = x

    if best_x is None:
        return None

    return best_x, best_sum

tot = 0
with open(fname, 'r') as lines:
    for line in [l.rstrip() for l in lines]:
        chunks = line.split(" ")

        goal_v = str_to_l(chunks[-1])

        buttons_v = [button_l_to_v(str_to_l(s), len(goal_v)) for s in chunks[1:(len(chunks) - 1)]]

        x, c = solve_min(goal_v, buttons_v)
        tot += c

print(f"Total minimum button presses: {tot}")
