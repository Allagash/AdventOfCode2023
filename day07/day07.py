# aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 07 - Camel Cards
# 2023


import pathlib
import sys
import re
import math
import functools 
from collections import defaultdict 


def parse(puzzle_input):
    """Parse input."""
    lines = [x.split() for x in puzzle_input.split('\n')]
    return lines

CARD_RANK  = "23456789TJQKA" # ace is always high
CARD_RANK2 = "J23456789TQKA" # ace is always high

def rankHands(hand):
    cards = defaultdict(lambda: 0)
    for h in hand:
        cards[h] += 1
    if len(cards) == 1:
        return 100 # 5 of kind
    elif len(cards) == 2: # full house or 4 of kind
        for c in cards:
            if cards[c] == 4:
                return 90 # 4 of kind
        return 80 # full house, ranked lower than 4 of kind
    elif len(cards) == 3: # 3 of kind or 2 pair
        for c in cards:
            if cards[c] == 3:
                return 70 # 3 of kind
        return 60 # 2 pair, ranked lower than 3 of kind
    elif len(cards) == 4: # one pair
        return 50
    else:
        return 40

def cmpCardsInOrder(hand1, hand2):
    #print("comparing cards in order", hand1, " and ", hand2) 
    for i in range(0, len(hand1)):
        rank1 = CARD_RANK.index(hand1[i])
        rank2 = CARD_RANK.index(hand2[i])
        if rank1 != rank2:
            return rank1 - rank2
    return 0

  
def mycmp(a, b): 
    #print("comparing ", a, " and ", b) 
    rank1 = rankHands(a[0])
    rank2 = rankHands(b[0])
    if rank1 != rank2: 
        return rank1 - rank2
    else: 
        return cmpCardsInOrder(a[0], b[0])


def part1(data):
    """Solve part 1."""
    s = sorted(data, key=functools.cmp_to_key(mycmp))
    print(*s, sep='\n')
    result = 0
    for i, x in enumerate(s):
        result += (i + 1) * int(x[1])
    # 250856581 is too low
    # 250760618 is too low
    return result


def part2(data):
    """Solve part 2."""


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
