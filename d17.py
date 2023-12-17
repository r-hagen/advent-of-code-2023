from heapq import heappop, heappush

grid = [list(map(int, line.strip())) for line in open("in")]

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3


def part1():
    global LEFT, RIGHT, UP, DOWN

    goal = (len(grid[0]) - 1, len(grid) - 1)
    seen = set()

    pq = []
    heappush(pq, (0, 1, 0, RIGHT, 1))
    heappush(pq, (0, 0, 1, DOWN, 1))
    while pq:
        l, x, y, d, s = heappop(pq)

        if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
            continue

        key = (x, y, d, s)
        if key in seen:
            continue
        seen.add(key)

        l += grid[y][x]

        if (x, y) == goal:
            return l

        if d == RIGHT:
            if s < 3:
                heappush(pq, (l, x + 1, y, d, s + 1))
            heappush(pq, (l, x, y - 1, UP, 1))
            heappush(pq, (l, x, y + 1, DOWN, 1))

        if d == LEFT:
            if s < 3:
                heappush(pq, (l, x - 1, y, d, s + 1))
            heappush(pq, (l, x, y - 1, UP, 1))
            heappush(pq, (l, x, y + 1, DOWN, 1))

        if d == UP:
            if s < 3:
                heappush(pq, (l, x, y - 1, d, s + 1))
            heappush(pq, (l, x - 1, y, LEFT, 1))
            heappush(pq, (l, x + 1, y, RIGHT, 1))

        if d == DOWN:
            if s < 3:
                heappush(pq, (l, x, y + 1, d, s + 1))
            heappush(pq, (l, x - 1, y, LEFT, 1))
            heappush(pq, (l, x + 1, y, RIGHT, 1))


def part2():
    global LEFT, RIGHT, UP, DOWN
    seen = set()

    pq = []
    heappush(pq, (0, 0, 0, 0, 0, 0))
    while pq:
        l, x, y, dx, dy, s = heappop(pq)

        if (x, y) == (len(grid[0]) - 1, len(grid) - 1) and s >= 4:
            return l

        if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
            continue

        key = (x, y, dx, dy, s)
        if key in seen:
            continue
        seen.add(key)

        if s < 10 and (dx, dy) != (0, 0):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                heappush(pq, (l + grid[ny][nx], nx, ny, dx, dy, s + 1))

        if s >= 4 or (dx, dy) == (0, 0):
            for ndx, ndy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndx, ndy) != (dx, dy) and (ndx, ndy) != (-dx, -dy):
                    nx = x + ndx
                    ny = y + ndy
                    if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                        heappush(pq, (l + grid[ny][nx], nx, ny, ndx, ndy, 1))


print("part1", part1())
print("part2", part2())
