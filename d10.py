from collections import deque

grid = open("in").read().strip().splitlines()

for y, row in enumerate(open("in").readlines()):
    for x, col in enumerate(row.strip()):
        if col == "S":
            sx, sy = (x, y)
            break
    else:
        continue
    break

loop = {(sx, sy)}
Q = deque([(sx, sy)])

maybe_s = {"|", "-", "J", "L", "7", "F"}

while Q:
    x, y = Q.popleft()
    tile = grid[y][x]

    if y > 0 and tile in "S|JL" and grid[y - 1][x] in "|7F" and (x, y - 1) not in loop:
        loop.add((x, y - 1))
        Q.append((x, y - 1))
        if tile == "S":
            maybe_s &= {"|", "J", "L"}

    if y < len(grid) - 1 and tile in "S|7F" and grid[y + 1][x] in "|JL" and (x, y + 1) not in loop:
        loop.add((x, y + 1))
        Q.append((x, y + 1))
        if tile == "S":
            maybe_s &= {"|", "7", "F"}

    if x > 0 and tile in "S-J7" and grid[y][x - 1] in "-LF" and (x - 1, y) not in loop:
        loop.add((x - 1, y))
        Q.append((x - 1, y))
        if tile == "S":
            maybe_s &= {"-", "J", "7"}

    if x < len(grid[0]) - 1 and tile in "S-FL" and grid[y][x + 1] in "-J7" and (x + 1, y) not in loop:
        loop.add((x + 1, y))
        Q.append((x + 1, y))
        if tile == "S":
            maybe_s &= {"-", "F", "L"}

print("part1", len(loop) // 2)

assert len(maybe_s) == 1
(S,) = maybe_s

grid = [row.replace("S", S) for row in grid]
grid = ["".join(tile if (x, y) in loop else "." for x, tile in enumerate(row)) for y, row in enumerate(grid)]

# print("\n".join(grid))

outside = set()

for y, row in enumerate(grid):
    within = False
    up = None
    for x, ch in enumerate(row):
        if ch == "|":
            assert up is None
            within = not within
        elif ch == "-":
            assert up is not None
        elif ch in "LF":
            assert up is None
            up = ch == "L"
        elif ch in "7J":
            assert up is not None
            if ch != ("J" if up else "7"):
                within = not within
            up = None
        elif ch == ".":
            pass
        else:
            raise RuntimeError("unexpected character (horizontal): {ch}")
        if not within:
            outside.add((x, y))

# for r in range(len(grid)):
#     for c in range(len(grid[r])):
#         print("#" if (r, c) in (outside - path) else ".", end="")
#     print()

print("part2", len(grid) * len(grid[0]) - len(outside | loop))
