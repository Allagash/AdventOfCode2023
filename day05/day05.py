# aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 05 - If You Give A Seed A Fertilizer
# 2023

# Part 2 takes 93 minutes to run on Apple M1 Max, MacBook Pro, 16-inch, 2021


import pathlib
import sys
import re
from collections import defaultdict 


def parse(puzzle_input):
    """Parse input."""
    groups = puzzle_input.split('\n\n')
    seeds = []
    maps = []
    for group in groups:
        if "seeds:" in group:
            seeds = [int(x) for x in group.split(" ")[1:]]
        else:
            lines = group.split("\n")
            mapping = []
            for line in lines:
                if "map:" not in line:
                    nums = line.split()
                    # tuple range, then amount to add
                    mapping.append((int(nums[1]), int(nums[1]) + int(nums[2]) - 1, int(nums[0]) - int(nums[1])))
            maps.append(mapping)
    #print(seeds)
    #print(maps)
    return seeds, maps

def transform(seed, maps):
    for mapping in maps:
        if (mapping[0] <= seed <= mapping[1]):
            return seed + mapping[2]
    return seed

def part1(data):
    """Solve part 1."""
    seeds = data[0]
    maps = data[1]
    min_val = sys.maxsize
    for s in seeds:
        r = s
        #print(s)
        for mapping in maps:
            r = transform(r, mapping)
            #print(r)
        min_val = min(min_val, r)
    return min_val

def part2Seeds(input):
    result = set()
    i = 0
    end = len(input)
    for i in range(0, end, 2):
        x = i
        newlist = input[i: i+2]
        print(f"newlist is {newlist}")
        y = {n for n in range(newlist[0], newlist[0] + newlist[1])}
        result.update(y)
    print (f"result size is {len(result)}")
#    myset = set(result)
 #   print (f"set size is {len(myset)}")
    return result


def part2(data):
    """Solve part 2."""
    seeds = part2Seeds(data[0])
    maps = data[1]
    min_val = sys.maxsize
    count = 0
    for s in seeds:
        count += 1
        if count % 10000 == 0:
            print(f"count = {count}")
        r = s
        #print(s)
        for mapping in maps:
            r = transform(r, mapping)
            #print(r)
        min_val = min(min_val, r)
    return min_val


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
