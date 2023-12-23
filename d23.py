from heapq import heappop, heappush

grid = open("in").read().splitlines()

poi = []
for r in [0, len(grid) - 1]:
    for c in range(0, len(grid[r])):
        if grid[r][c] == ".":
            poi.append((r, c))
start, end = poi

seen = dict()
steps = set()
q = [(0, start, [start])]
while q:
    s, pos, path = heappop(q)
    s = -1 * s

    if pos == end:
        steps.add(s)
        continue

    if pos in seen and seen[pos] > steps:
        continue
    seen[pos] = steps

    r, c = pos
    if grid[r][c] == ".":
        for nr, nc in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]) and (nr, nc) not in path and grid[nr][nc] != "#":
                heappush(q, (-1 * (s + 1), (nr, nc), path + [(nr, nc)]))
    elif grid[r][c] == ">":
        nr, nc = r, c + 1
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]) and (nr, nc) not in path and grid[nr][nc] != "#":
            heappush(q, (-1 * (s + 1), (nr, nc), path + [(nr, nc)]))
    elif grid[r][c] == "v":
        nr, nc = r + 1, c
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]) and (nr, nc) not in path and grid[nr][nc] != "#":
            heappush(q, (-1 * (s + 1), (nr, nc), path + [(nr, nc)]))

print("part1", max(steps))
