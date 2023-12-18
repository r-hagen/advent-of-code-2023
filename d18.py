from collections import deque


def part1():
    M = {}
    p = (0, 0)
    for line in open("in").read().splitlines():
        d, a, _ = line.split()
        for _ in range(int(a)):
            dx = 1 if d in "R" else -1 if d in "L" else 0
            dy = 1 if d in "D" else -1 if d in "U" else 0
            p = (p[0] + dx, p[1] + dy)
            M[p] = True

    xmin, xmax = min(M, key=lambda t: t[0])[0], max(M, key=lambda t: t[0])[0]
    ymin, ymax = min(M, key=lambda t: t[1])[1], max(M, key=lambda t: t[1])[1]

    q = deque()
    nbs = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            if (x, y) in M:
                continue
            if sum([1 if (x + dx, y + dy) in M else 0 for dx, dy in nbs]) == len(nbs) - 1:
                q.append((x, y))

    while q:
        x, y = q.popleft()
        if (x, y) in M:
            continue
        M[(x, y)] = True
        for dx, dy in nbs:
            q.append((x + dx, y + dy))

    return len(M)


print("part1", part1())
