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
