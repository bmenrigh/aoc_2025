# [Advent of Code 2025](https://adventofcode.com/2025)

My goal this year it so solve all challenges in Python. I want the runtime of each solution to be as short as possible, within reason. Python isn't exactly super fast so this will favor algorithmically efficient approaches. No external libraries will be used.

---

## Day 01: \*\*

**Rotary dial combination. Count number of times the dial pointed at zero, or crossed zero.**

Part 1: `10 ms`

Part 2: `10 ms`


## Day 02: \*\*

**Look for numerical IDs with patterns like 6464 or 123123, or 777, etc.**

For the part 2 redux, I turned the problem around and instead of checking if each number in the given ranges has a pattern in the digits, I instead generated all possible digit patterns and checked if they were in the given ranges.

Part 1: `10 ms`

Part 2: `1880 ms` (Python 3.12.11) / `342 ms` (PyPy 7.3.19)

Part 2 redux: `161 ms` (Python 3.12.11) / `25 ms` (PyPy 7.3.19)


## Day 03: \*\*

**Largest number of given length constructable from a string of digits, allowing for some digits to be skipped.**

I spotted the simple greedy algorithm for part 1 almost immediately. For part two, applying induction on the reasoning in part 1 extends the reasoning used for 2-digit numbers to any number of digits. Part 2 is probably computationally infeasible without spotting the greedy algorithm.

Part 1: `10 ms`

Part 2: `10 ms`


## Day 04: \*\*

**Count items in grid with fewer than 4 neighbors. Later, see how many items can be removed based on their neighbors, where removable of an item may make a previously unremovable one become removable.**

Part 2 can be done efficiently by removing an item, and then updating cached neighbor counts only for its 8 neighbors. Once updated, then only checking if any of those 8 neighbors can now be removed. Since removal criteria is localized, the effect of removal is also localized, and this keeps the amount of checking after changes low.

Part 1: `16 ms`

Part 2: `29 ms`


## Day 05: \*\*

**Take list of given numerical ranges like 3-4, 6-10, 7-12, and another list of number, check if the numbers are in the ranges. Later, find the total span of all the ranges (overlaps not counted).**

I did not see an efficient way to do part 1 without first merging overlapping ranges. Once all the ranges are coalesced, binary search can quickly find which range a number may be in. To my surprise, this merging effort ended up instantly solving part 2 which makes the code to my part 1 substantially longer than part 2.

Part 1: `9 ms`

Part 2: `9 ms`


## Day 06: \*\*

**Take a space-separated ASCII table of numbers and mathematical operations and apply the operation in the bottom row to the numbers in the column above it. Later interpret the numbers in the column above not as read row-by-row but read vertically as sub-column of characters within the column.**

There is no opportunity for cleverness in this problem.

Part 1: `13 ms`

Part 2: `16 ms`


## Day 07: \*\*

**Given a grid indicating free space, a downward "beam", and "beam splitters" track how many beam splitters are hit by the beam on the way down. Later, count the total number of unique paths from top to bottom.**

I really liked this problem. It looks like a tool for recursion but it's quite simple to just process row-by-row. Counting the number of unique paths can also be done row-by-row by tracking the number of copies of a beam in each given location on the grid. Then each row propogating that number down or into two copies when all those beams hit a splitter. This approach reminds me of the solution approach to Project Euler's [Problem 18 "Maximum Sum Path I"](https://projecteuler.net/problem=18) and [Problem 67 "Maximum Sum Path II"](https://projecteuler.net/problem=67).

Part 1: `10 ms`

Part 2: `10 ms`


## Day 08: \*\*

**Given a list of points in 3-space, connect the closest N to find the largest M connected groups formed. Later, connect N points in order of closest pairs until all N points form one connected group.***

This problem has a very "computer science" feel to it. With 1000 points (the N given in the problem), and 1000 connections (the M given in the problem), it may be possible to find the nearest 1000 pairs without checking the full `O(N^2)` pairs for distance. That said, I'm not sure how to do so efficiently in a way that's guaranteed to be correct. As such, I opted to calculate the distance for all pairs. I'm not happy with the runtime of my solutions. But, without a clear idea for how to improve the algorithm, and the general slowness of python, I've begrudgingly accepted them for now.

Part 1: `501 ms`

Part 2: `552 ms`


## Day 09: \*\*

**Given a set of points, find the largest rectangle defined by diagonally opposite points. For part 2, given a set of points that form a "grid-aligned" looping perimeter of some shape, what is the largest rectangle contained in the shape defined by two diagonally opposite perimeter points.**

For part 1, my key insight was to make a list of every y coordinate for a given x, and every x coordinate for a given y. This allowed quickly finding the widest horizontal and vertical spans available once one corner was chosen.

For part 2, my key insight was to make a list of all horizontal and vertical edges of the perimeter. A box is contained entirely inside of the shape if neither of the two vertical sides of the box cross a horizontal perimeter, and neither of the two horizontal sides of the box cross a vertical perimeter line.

Part 1: `20 ms`

Part 2: `389 ms`


## Day 10: \*

**Given a set of vectors as a basis, and a goal vector, find the minimum number of basis vectors needed to sum to the goal vector. For part 1 this is all done essentially mod 2 so the problem reduces to XOR and is equivalent to a 1-dimensional version of "Lights Out".**

For part 1 I knew immediately that this was essentially Lights Out in 1 dimension and that no vector would need to be used more than once. I encoded the vectors as bit fields and used XOR with a depth-limited backtracking search.

For part 2 I modified my search to use vectors and sums rather than integers and XOR. In principle I think the solution is correct but the runtime would be age-of-the-universe levels of bad. Many of the problems have the number of basis vectors matching the dimensionality so in these cases, it's just a system of equations (assuming the all are independent).

I explained the vector problem to ChatGPT and had it write a pure-python Gaussian elimination-based solution. I *strongly* suspect that I've overlooked some nice "trick" because the problem is much simpler than general vectors (the basis vectors are always 0s and 1s).

Part 1: `13ms`
