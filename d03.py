G = [[c for c in r.strip()] for r in open("in").readlines()]
L = {}

HEIGHT = len(G)
WIDTH = len(G[0])


def is_adjacent_to_symbol(y, x, n):
    y1 = y - 1 if y - 1 >= 0 else 0
    y2 = y + 1 if y + 1 < HEIGHT else HEIGHT - 1
    x1 = x - 1 if x - 1 >= 0 else 0
    x2 = x + n if x + n < WIDTH else WIDTH - 1
    for r in range(y1, y2 + 1):
        for c in range(x1, x2 + 1):
            if G[r][c] != "." and not G[r][c].isnumeric():
                # keep track of gears for part 2
                if G[r][c] == "*":
                    if (r, c) in L:
                        L[(r, c)].append(gear(y, x, n))
                    else:
                        L[(r, c)] = [gear(y, x, n)]
                return True
    return False


def gear(y, x, n):
    return int("".join(G[y][x : x + n]))


def part1():
    ans = 0

    r = 0
    c = 0
    while r < HEIGHT:
        while c < WIDTH:
            if not G[r][c].isnumeric():
                c += 1
                continue
            w = 1
            while c + w < WIDTH and G[r][c + w].isnumeric():
                w += 1
            if is_adjacent_to_symbol(r, c, w):
                ans += gear(r, c, w)
            c += w
        c = 0
        r += 1

    return ans


def part2():
    ans = 0
    for _, gs in L.items():
        if len(gs) == 2:
            ans += gs[0] * gs[1]
    return ans


print("part1", part1())
print("part2", part2())
