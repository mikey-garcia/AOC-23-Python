def _is_symbol(char):
    if char.isdigit() or char == '.':
        return False
    return True

def _is_gear(char):
    if char == "*":
        return True
    return False  

def part1(lines):
    """
    Not my best work lol
    """
    # Load all lines into memory to do this really easily.
    LEN_LINE = 140
    schematic=''.join(lines)
    same_number=False
    curr_number = ''
    numbers=[]
    # save all numbers and their indices
    for i, char in enumerate(schematic):

        if not char.isdigit():
            same_number=False
            if curr_number != '':
                if save_number:
                    numbers.append(curr_number)
                curr_number = ''
            save_number=False
            continue

        # Don't double count numbers. Simply construct your number with the next digit char.
        curr_number+=char
        if same_number:
            continue

        # Top edge
        if i < LEN_LINE:
            if  _is_symbol(schematic[i-1]) or \
                _is_symbol(schematic[i+1]) or \
                _is_symbol(schematic[i+LEN_LINE-1]) or\
                _is_symbol(schematic[i+LEN_LINE]) or\
                _is_symbol(schematic[i+LEN_LINE+1]):
                #curr_number+=char
                save_number=True
                same_number=True

        # Bottom Edge
        elif i > LEN_LINE*(LEN_LINE-1):
            if  _is_symbol(schematic[i-1]) or \
                _is_symbol(schematic[i+1]) or \
                _is_symbol(schematic[i-LEN_LINE-1]) or\
                _is_symbol(schematic[i-LEN_LINE]) or\
                _is_symbol(schematic[i-LEN_LINE+1]):
                #curr_number+=char
                save_number=True
                same_number=True

        # Left Edge
        elif i % LEN_LINE == 0:
            if  _is_symbol(schematic[i+1]) or \
                _is_symbol(schematic[i-LEN_LINE]) or\
                _is_symbol(schematic[i-LEN_LINE+1]) or\
                _is_symbol(schematic[i+LEN_LINE]) or\
                _is_symbol(schematic[i+LEN_LINE+1]):
                #curr_number+=char
                save_number=True
                same_number=True

        # Right Edge
        elif i % LEN_LINE == LEN_LINE-1:
            if  _is_symbol(schematic[i-1]) or \
                _is_symbol(schematic[i-LEN_LINE]) or\
                _is_symbol(schematic[i-LEN_LINE-1]) or\
                _is_symbol(schematic[i+LEN_LINE]) or\
                _is_symbol(schematic[i+LEN_LINE-1]):
                #curr_number+=char
                save_number=True
                same_number=True

        # All other cases
        else:
            if  _is_symbol(schematic[i+1]) or \
                _is_symbol(schematic[i-1]) or\
                _is_symbol(schematic[i-LEN_LINE]) or\
                _is_symbol(schematic[i-LEN_LINE-1]) or\
                _is_symbol(schematic[i-LEN_LINE+1]) or\
                _is_symbol(schematic[i+LEN_LINE]) or\
                _is_symbol(schematic[i+LEN_LINE-1]) or\
                _is_symbol(schematic[i+LEN_LINE+1]):
                #curr_number+=char
                save_number=True
                same_number=True
    numbers = list(map(int,numbers))
    return sum(numbers)

def part2(lines):
    part2=0
    def is_neighbor(gear_index, char_index): # okay just make the neighbor check a function bc that stuff earlier was really obnoxious
        LEN_LINE = 140
        UP = gear_index - LEN_LINE
        DOWN = gear_index + LEN_LINE
        LEFT = gear_index - 1
        RIGHT = gear_index + 1 
        UPLEFT = gear_index - LEN_LINE - 1
        DOWNLEFT = gear_index + LEN_LINE - 1
        UPRIGHT = gear_index - LEN_LINE + 1
        DOWNRIGHT = gear_index + LEN_LINE + 1
        neighbors = [UP, DOWN, LEFT, RIGHT, UPLEFT, DOWNLEFT, UPRIGHT, DOWNRIGHT]
        if char_index in neighbors:
            return True
        return False

    # Load all lines into memory to do this really easily.
    schematic=''.join(lines)
    curr_number = ''
    numbers={} # Starting Index : Digit
    gears = [] # Index

    # save all numbers and their indices
    for i, char in enumerate(schematic):
        if _is_gear(char):
            gears.append(i)
        if not char.isdigit(): # Either a '.' slide, or the end of a number (save that number)
            if curr_number != '':
                numbers[i-len(curr_number)] = curr_number
                curr_number = ''
            continue
        curr_number+=char

    gear_dict = {}
    for gear in gears:
        gear_dict[gear] = []
        for i, val in numbers.items():
            for k in range(len(val)):
                if is_neighbor(gear, i+k):
                    gear_dict[gear].append(int(val))
                    break

    for g in gear_dict.values():
        if len(g) == 2:
            part2 += g[0] * g[1]
    return part2