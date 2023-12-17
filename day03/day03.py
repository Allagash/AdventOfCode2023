# aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 03 - Gear Ratios
# 2023


import pathlib
import sys
import re


def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')
    return lines

def getSymbols(lines):
    symLocns = []
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c != '.' and (c < '0' or c > '9'):
                symLocns.append((row, col))
    return symLocns

def getAsterisks(lines):
    symLocns = []
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            if c == '*':
                symLocns.append((row, col))
    return symLocns
    
surroundPos = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
    ]
    
def getDigitLocns(symbolLocns, lines):
    maxRow = len(lines) - 1
    maxCol = len(lines[0]) - 1
    digitsToScan = set()
    for sym in symbolLocns:
        for surround in surroundPos:
            checkPos = (sym[0] + surround[0], sym[1] + surround[1])
            if (checkPos[0] >= 0 and checkPos[0] <= maxRow and 
                checkPos[1] >=0 and checkPos[1] <= maxCol):
                checkChar = lines[checkPos[0]][checkPos[1]]
                if (checkChar.isdigit()):
                    digitsToScan.add(checkPos)
    return digitsToScan

def getGearLocns(symbolLocns, lines):
    maxRow = len(lines) - 1
    maxCol = len(lines[0]) - 1
    digitsToScan = set()
    for sym in symbolLocns:
        numbers = set()
        for surround in surroundPos:
            checkPos = (sym[0] + surround[0], sym[1] + surround[1])
            if (checkPos[0] >= 0 and checkPos[0] <= maxRow and 
                checkPos[1] >=0 and checkPos[1] <= maxCol):
                checkChar = lines[checkPos[0]][checkPos[1]]
                if (checkChar.isdigit()):
                    numbers.add(getFirstDigit(checkPos, lines))
        if len(numbers) == 2:
            numList = list(numbers)        
            digitsToScan.add((numList[0], numList[1]))             
    return digitsToScan

def getGearRatios(digitsToScan, lines):
    ratios = []
    for numList in digitsToScan:
        ratio = getNumber(numList[0], lines) * getNumber(numList[1], lines)
        ratios.append(ratio)
    return ratios


def getFirstDigit(pos, lines):
    row = pos[0]
    col = pos[1]
    while col > 0 and lines[row][col - 1].isdigit():
        col -= 1
    return (row, col)


def getFirstDigitLocns(digitsToScan, lines):
    startDigits = set()
    for pos in digitsToScan:
        startDigits.add(getFirstDigit(pos, lines))
    return startDigits

def getNumber(pos, lines):
    num = 0
    maxCol = len(lines[0]) - 1
    row = pos[0]
    col = pos[1]
    while col <= maxCol and lines[row][col].isdigit():
        num = num * 10 + int(lines[row][col])
        col += 1
    return num

def getNumbers(startDigits, lines):
    numbers = []
    for pos in startDigits:        
        numbers.append(getNumber(pos, lines))
    return numbers

def part1(data):
    """Solve part 1."""
    # print(data)
    symbolLocns = getSymbols(data)
    digitsToScan = getDigitLocns(symbolLocns, data)
    startDigits = getFirstDigitLocns(digitsToScan, data)
    numbers = getNumbers(startDigits, data)
    #print(numbers)
    return sum(numbers)

def part2(data):
    """Solve part 2."""
    asterisks = getAsterisks(data)
    digitsToScan = getGearLocns(asterisks, data)
    ratios = getGearRatios(digitsToScan, data)
    return sum(ratios)


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
