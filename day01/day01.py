# aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 1, Trebuchet?!
# 2023

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.split('\n')


def part1(data):
    """Solve part 1."""
    result = 0
    for line in data:
        first = -1
        last = -1
        for c in line: 
            if c.isdigit():
                last = int(c)
                if first < 0:
                    first = int(c)
        result = result + 10*first + last
    return result

# no zeros

digitvals = [("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6), ("7", 7), ("8", 8), ("9", 9),
        ("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9)]

def findFirstDigit(line):
    pos = -1
    result = 0
    for d in digitvals:
        #print(f'{d}')
        idx = line.find(d[0])
        if idx >= 0 and (pos < 0 or idx < pos):
            #print(f'pos = {pos}, idx = {idx}')
            pos = idx
            result = d[1]
            #print(f'result = {result}')
    return result

def findLastDigit(line):
    pos = -1
    for d in digitvals:
        idx = line.rfind(d[0])
        if idx >= 0 and idx > pos:
            pos = idx
            result = d[1]
    return result

def part2(data):
    """Solve part 2."""
    result = 0
    for line in data:
        first = findFirstDigit(line)
        last = findLastDigit(line)
        #print(line, first, last)
        result = result + 10*first + last
    return result

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
