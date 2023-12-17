# aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 04 - Scratchcards
# 2023


import pathlib
import sys
import re
from collections import defaultdict 


def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')
    result = []
    for line in lines:
        numStrings = line.split(': ')[1].split(' | ')
        cards = []
        for n in numStrings:
            q = set([int(x) for x in n.split()])
            #print(q)
            cards.append(q)
        result.append(cards)
    #print(result)
    return result


def part1(data):
    """Solve part 1."""
    result = []
    for d in data:
        matches = len(d[0].intersection(d[1]))
        if matches > 0:
            result.append(2 ** (matches - 1))
        #print(matches)
    #print(result)
    return sum(result)

def def_value(): 
    return 1

def part2(data):
    """Solve part 2."""
    result = []
    bonus = defaultdict(def_value)
    mysum = []
    for i in range(len(data)):
        mysum.append(1)
    for idx, d in enumerate(data):
        matches = len(d[0].intersection(d[1]))
        #print(idx, matches)
        if matches > 0:
            for j in range(mysum[idx]):
                for i in range(matches):
                    mysum[idx + i + 1] += 1
    #print(mysum)
    return sum(mysum)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
