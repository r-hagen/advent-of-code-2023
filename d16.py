grid = open("in").read().strip().splitlines()

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


def energize(x, y, d):
    global RIGHT, DOWN, LEFT, UP
    energized = {}

    seen = set()
    queue = [(x, y, d)]
    while queue:
        x, y, d = queue.pop(0)

        if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
            continue

        energized[(x, y)] = True

        if (x, y, d) in seen:
            continue

        seen.add((x, y, d))

        if grid[y][x] in ".":
            if d == RIGHT:
                queue.append((x + 1, y, d))
            if d == DOWN:
                queue.append((x, y + 1, d))
            if d == LEFT:
                queue.append((x - 1, y, d))
            if d == UP:
                queue.append((x, y - 1, d))

        if grid[y][x] in "|":
            if d == UP:
                queue.append((x, y - 1, d))
            if d == DOWN:
                queue.append((x, y + 1, d))
            if d in [RIGHT, LEFT]:
                queue.append((x, y - 1, UP))
                queue.append((x, y + 1, DOWN))

        if grid[y][x] in "-":
            if d == LEFT:
                queue.append((x - 1, y, d))
            if d == RIGHT:
                queue.append((x + 1, y, d))
            if d in [UP, DOWN]:
                queue.append((x - 1, y, LEFT))
                queue.append((x + 1, y, RIGHT))

        if grid[y][x] in "/":
            if d == RIGHT:
                queue.append((x, y - 1, UP))
            if d == DOWN:
                queue.append((x - 1, y, LEFT))
            if d == LEFT:
                queue.append((x, y + 1, DOWN))
            if d == UP:
                queue.append((x + 1, y, RIGHT))

        if grid[y][x] in "\\":
            if d == RIGHT:
                queue.append((x, y + 1, DOWN))
            if d == DOWN:
                queue.append((x + 1, y, RIGHT))
            if d == LEFT:
                queue.append((x, y - 1, UP))
            if d == UP:
                queue.append((x - 1, y, LEFT))

    return len(energized)


print("part1", energize(0, 0, RIGHT))

total = 0
assert len(grid) == len(grid[0])
sz = len(grid)
for n in range(sz):
    total = max(total, energize(n, 0, DOWN))
    total = max(total, energize(n, sz - 1, UP))
    total = max(total, energize(0, n, RIGHT))
    total = max(total, energize(sz - 1, n, LEFT))
print("part2", total)
