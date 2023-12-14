dish = [list(line.strip()) for line in open("in").readlines()]


def tilt(d):
    flipped = list(zip(*d))
    tilted = []
    for column in flipped:
        T = ["."] * len(column)
        e = 0
        for i, r in enumerate(column):
            if r == "#":
                T[i] = "#"
                e = i + 1
            if r == "O":
                T[e] = "O"
                e = e + 1
        tilted.append(T)
    return list(zip(*tilted))


def part1():
    tilted = tilt(dish)
    return sum([row.count("O") * i for i, row in enumerate(tilted[::-1], 1)])


print("part1", part1())
