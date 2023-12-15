input = open("in").read().strip().split(",")


def hash(s):
    value = 0
    for ch in s:
        value += ord(ch)
        value *= 17
        value %= 256
    return value


def part1(steps):
    total = 0
    for step in steps:
        total += hash(step)
    return total


def part2(steps):
    boxes = [[] for _ in range(256)]
    for s in steps:
        if "-" in s:
            label = s[:-1]
            h = hash(label)
            i = next((i for i, (l, _) in enumerate(boxes[h]) if l == label), -1)
            if i != -1:
                boxes[h].pop(i)
        if "=" in s:
            label, focal = s.split("=")
            focal = int(focal)
            h = hash(label)
            i = next((i for i, (l, _) in enumerate(boxes[h]) if l == label), -1)
            if i != -1:
                boxes[h][i] = (label, focal)
            else:
                boxes[h].append((label, focal))

    total = 0
    for bi, b in enumerate(boxes, 1):
        for li, (l, f) in enumerate(b, 1):
            total += bi * li * f
    return total


print("part1", part1(input))
print("part2", part2(input))
