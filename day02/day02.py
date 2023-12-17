# aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 02 - Cube Conundrum
# 2023


import pathlib
import sys
import re


def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')
    #print(lines)
    data = []
    for line in lines:
        grabs = line.split(': ')[1].split('; ')
        colorCount = {'red': 0, 'green': 0, 'blue': 0}
        for grab in grabs:
            color = grab.split(', ')
            for c in color:
                m = re.match("(\d+) (\w+)", c)
                currColor = m.groups()[1]
                currCount = int(m.groups()[0])
                colorCount[currColor] = max(currCount, colorCount[currColor]) 
        data.append(colorCount)
    return data

def possible(colorCount):
    # only 12 red cubes, 13 green cubes, and 14 blue cubes?
    return colorCount['red'] <= 12 and colorCount['green'] <= 13 and colorCount['blue'] <= 14


def power(colorCount):
    return colorCount['red'] * colorCount['green'] * colorCount['blue']


def part1(data):
    """Solve part 1."""
    # print(data)
    sum = 0
    for idx, x in enumerate(data):
        if (possible(x)):
            sum = sum + idx + 1 # index is 1-based in data
    return sum

def part2(data):
    """Solve part 2."""
    sum = 0
    for idx, x in enumerate(data):
        sum = sum + power(x)
    return sum

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
