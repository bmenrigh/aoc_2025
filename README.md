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

**Largest number in a string of numbers such that some digits can be skipped.**

I spotted the simple greedy algorithm for part 1 almost immediately. For part two, applying induction on the reasoning in part 1 extends the reasoning used for 2-digit numbers to any number of digits. Part 2 is probably computationally infeasible without spotting the greedy algorithm.

Part 1: `10 ms`

Part 2: `10 ms`
