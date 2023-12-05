# Advent of Code Submissions (Python) for 2023
Don't make fun of me im trying my best

## Usage
If you don't already have a folder created, it will create a folder "dayX" with input.txt and solution.py based off of the day you input.

Will also run your solution.py and print your answers.
```bash
aoc [day]
```

## How to setup
Inside of ~/.bashrc...

```bash
# custom bash function of Advent of Code
aoc() {
    python3 aoc.py "$1"
}
```