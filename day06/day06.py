# aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 06 - Wait For It
# 2023


import pathlib
import sys
import re
import math
from collections import defaultdict 


def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')
    times = lines[0].split()[1:]
    dists = lines[1].split()[1:]
    time1 = [int(x) for x in times]
    dist1 = [int(x) for x in dists]
    time2 = int("".join(times))
    dist2 = int("".join(dists))
    return time1, dist1, time2, dist2

def calcWinningWays(time, dist):
    # quadratic formula
    minVal = (-time + math.sqrt(time * time - 4.0 * -1 * -dist) ) / -2.0
    maxVal = (-time - math.sqrt(time * time - 4.0 * -1 * -dist) ) / -2.0
    print(time, dist, minVal, maxVal)
    newMin = round(minVal + 0.5)
    if (newMin == minVal): # inequality
        newMin += 1
    newMax = int(maxVal)
    if (newMax == maxVal):
        newMax -= 1
    print(f"minVal is {newMin}, max is {newMax}")
    return newMax - newMin + 1 # if range is [2, 5], then 2, 3, 4, 5, so 4 vals = 5 - 2 +

def part1(data):
    """Solve part 1."""
    # print(data[0], data[1])
    results = []
    for idx, x in enumerate(data[0]):
        results.append(calcWinningWays(x, data[1][idx]))
    print(results)
    return math.prod(results)


def part2(data):
    """Solve part 2."""
    time = data[0]
    dist = data[1]
    print(f"part2: time = {time}, dist = {dist}")
    return calcWinningWays(time, dist)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data[0:2])
    solution2 = part2(data[2:])

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
