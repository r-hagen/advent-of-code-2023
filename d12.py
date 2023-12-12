cache = {}


def arrangements(s, g):
    if s == "":
        return 1 if g == () else 0

    if g == ():
        return 0 if "#" in s else 1

    key = (s, g)
    if key in cache:
        return cache[key]

    result = 0

    if s[0] in ".?":
        result += arrangements(s[1:], g)

    if s[0] in "#?":
        if (
            g[0] <= len(s)  # enough springs left
            and "." not in s[: g[0]]  # no operational springs in block
            and (g[0] == len(s) or s[g[0]] != "#") # next spring after must be operational
        ):
            result += arrangements(s[g[0] + 1 :], g[1:])

    cache[key] = result

    return result


def part1():
    total = 0
    for line in open("in"):
        springs, groups = line.split()
        groups = tuple(map(int, groups.split(",")))
        total += arrangements(springs, groups)
    return total


def part2():
    total = 0
    for line in open("in"):
        springs, groups = line.split()
        groups = tuple(map(int, groups.split(",")))
        springs = "?".join([springs] * 5)
        groups = groups * 5
        total += arrangements(springs, groups)
    return total


print("part1", part1())
print("part2", part2())
