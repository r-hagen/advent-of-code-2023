lines = [x.strip() for x in open("in").readlines()]


def parse_cards(line):
    parts = line.split(": ")[1].split(" | ")
    winning = list(map(int, [x for x in parts[0].split(" ") if x]))
    have = list(map(int, [x for x in parts[1].split(" ") if x]))
    return (winning, have)


def part1():
    ans = 0
    for line in lines:
        winning, have = parse_cards(line)
        points = 0
        for card in have:
            if card in winning:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        ans += points
    return ans


def part2():
    scratchcards = [1] * len(lines)
    for i, line in enumerate(lines):
        winning, have = parse_cards(line)
        matching = sum([1 for card in have if card in winning])
        for n in range(i + 1, i + matching + 1):
            scratchcards[n] += scratchcards[i]
    return sum(scratchcards)


print("part1", part1())
print("part2", part2())
