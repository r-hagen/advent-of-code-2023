from collections import deque

grid = open("in").read().strip().splitlines()
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == "S":
            start = (r, c)

plots = {start}
seen = {start}
q = deque([(64, start)])

while q:
    steps, pos = q.popleft()

    if steps < 0:
        continue
    if steps == 0:
        plots.add(pos)

    key = (steps, pos)
    if key in seen:
        continue
    seen.add(key)

    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nr, nc = pos[0] + dr, pos[1] + dc
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
            continue
        if grid[nr][nc] != "#":
            q.append((steps - 1, (nr, nc)))

print("part1", len(plots))
