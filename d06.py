def part1():
    lines = open("in").readlines()
    times = list(map(int, lines[0].split(":")[1].split()))
    distances = list(map(int, lines[1].split(":")[1].split()))

    ans = 1
    for t, d in zip(times, distances):
        ways = 0
        for th in range(1, t - 1):
            dh = th * (t - th)
            if dh > d:
                ways += 1
        ans = ans * ways

    return ans


def part2():
    lines = open("in").readlines()
    t = int("".join(lines[0].split(":")[1].split()))
    d = int("".join(lines[1].split(":")[1].split()))

    ways = 0
    for th in range(1, t - 1):
        dh = th * (t - th)
        if dh > d:
            ways += 1

    return ways


print("part1", part1())
print("part2", part2())
