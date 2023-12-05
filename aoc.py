"""
Advent of Code Solution Loader for Python Implementations.

Inside of ~/.bashrc...

# custom bash function of Advent of Code
aoc() {
    python3 aoc.py "$1"
}

Usage: aoc [day]
"""
import os
import utils
import importlib
import argparse

def run(day_number="1"):
    if not os.path.isdir(f"day{day_number}"): # only do GET request once bc being nice is nice :) 
        utils.make_folder(day_number)

    input = utils.read_text_file(os.path.join(f"day{day_number}", "input.txt")) 
    sol = importlib.import_module(f"day{day_number}"+".solution")

    print("Part 1:", sol.part1(input))
    print("Part 2:", sol.part2(input))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Advent of Code solutions')
    parser.add_argument('day', metavar='day', type=int,
                help="Which day of Advent of Code you're on.")
    args = parser.parse_args()
    run(str(args.day))





