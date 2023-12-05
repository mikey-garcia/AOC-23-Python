def part1(cases):
    part1=0
    for case in cases:
        nums = [chr(i) for i in case.encode('ascii') if i<58 and i>47]
        part1+=int(nums[0] + nums[-1])
    return part1

def part2(cases):
    part2=0
    spelled = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    for case in cases:
        case_nums = []
        buf = []
        for i in range(len(case)):
            char = case[i]
            buf.append(char)
            for num in spelled:
                    if num in ''.join(buf):
                        case_nums.append(spelled[num])
                        buf=[buf[-1]] # only save the last one in case of overlap like "twone"
            if char.isdigit():
                case_nums.append(char)
        part2+=int(case_nums[0] + case_nums[-1])
    return part2