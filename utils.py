import os
import requests

def _create_folder(day_number):
    # make dir
    path = os.path.join(os.getcwd(), f"day{day_number}")
    try:
        os.mkdir(path)
    except OSError as error: # if folder already exists
        print(error)
    # make template solution.py
    template = """def part1(cases):
    part1=0

    return part1

def part2(cases):
    part2=0

    return part2
"""
    with open(os.path.join(os.getcwd(), f"day{day_number}", "solution.py"), 'w') as f:
        f.write(template)
    return
    
def _make_input(day_number):
    try:
        session_cookie = open("../session_cookie.txt", 'r').readline().strip() 
    except:
        print("Provide a session cookie, and place it in this directory as session_cookie.txt")
    headers = {'Cookie': session_cookie}
    r = requests.get(f"https://adventofcode.com/2023/day/{day_number}/input", headers=headers)
    with open(os.path.join(os.getcwd(), f"day{day_number}", "input.txt"), 'w') as f:
        f.write(r.text)
    return

def make_folder(day_number):
    _create_folder(day_number)
    _make_input(day_number)
    return

def read_text_file(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f]
    


