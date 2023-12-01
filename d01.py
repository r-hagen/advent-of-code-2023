lines = [x.strip() for x in open("in").readlines()]


def calibration_value(line):
    first = None
    last = None

    i = 0
    j = len(line) - 1
    while i < len(line) and j >= 0:
        if first is None and line[i].isnumeric():
            first = line[i]
        if last is None and line[j].isnumeric():
            last = line[j]
        if first and last:
            break
        i = i + 1
        j = j - 1

    return int(first + last)


def part1(lines):
    return sum([calibration_value(line) for line in lines])


def expand_literals(line):
    L2N = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    expanded = ""
    for i, char in enumerate(line):
        if char.isnumeric():
            expanded += char
        else:
            for literal in L2N.keys():
                if line[i:].startswith(literal):
                    expanded += L2N[literal]
    return expanded


def part2(lines):
    return sum([calibration_value(expand_literals(line)) for line in lines])


print("part1", part1(lines))
print("part2", part2(lines))
