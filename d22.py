import math

blocks = {}
for id, line in enumerate(open("in").read().splitlines(), 1):
    start, end = line.split("~")
    x1, y1, z1 = tuple(map(int, start.split(",")))
    x2, y2, z2 = tuple(map(int, end.split(",")))

    is_horizontal = z1 == z2
    # print(f"Line {id} is", "horizontal" if is_horizontal else "vertical")

    if is_horizontal:
        assert z1 == z2
        xmin, xmax = min(x1, x2), max(x1, x2)
        ymin, ymax = min(y1, y2), max(y1, y2)
        for y in range(ymin, ymax + 1):
            for x in range(xmin, xmax + 1):
                assert (x, y, z1) not in blocks
                blocks[(x, y, z1)] = id
    else:
        assert y1 == y2
        xmin, xmax = min(x1, x2), max(x1, x2)
        zmin, zmax = min(z1, z2), max(z1, z2)
        for z in range(zmin, zmax + 1):
            for x in range(xmin, xmax + 1):
                assert (x, y1, z) not in blocks
                blocks[(x, y1, z)] = id


def plot_xz(blocks):
    zmin, zmax = min(z for _, _, z in blocks), max(z for _, _, z in blocks)
    xmin, xmax = min(x for x, _, _ in blocks), max(x for x, _, _ in blocks)
    print("x".rjust(math.ceil((xmax + 1) / 2)))
    print("".join([str(x) for x in range(xmin, xmax + 1)]))
    for z in range(zmax, zmin - 1, -1):
        for x in range(xmin, xmax + 1):
            y = max([yy for xx, yy, zz in blocks if xx == x and zz == z] or [0])
            print(blocks.get((x, y, z), "."), end="")
        print(f" {z}", end="")
        print(" z" if z == math.ceil((zmax + 1) / 2) else "", end="")
        print()


def plot_yz(blocks):
    zmin, zmax = min(z for _, _, z in blocks), max(z for _, _, z in blocks)
    ymin, ymax = min(y for _, y, _ in blocks), max(y for _, y, _ in blocks)
    print("y".rjust(math.ceil((ymax + 1) / 2)))
    print("".join([str(y) for y in range(ymin, ymax + 1)]))
    for z in range(zmax, zmin - 1, -1):
        for y in range(ymin, ymax + 1):
            x = max([xx for xx, yy, zz in blocks if yy == y and zz == z] or [0])
            print(blocks.get((x, y, z), "."), end="")
        print(f" {z}", end="")
        print(" z" if z == math.ceil((zmax + 1) / 2) else "", end="")
        print()


settled = False
while not settled:
    settled = True
    ids = set(blocks.values())
    for id in ids:
        bricks = [k for k, v in blocks.items() if v == id]
        is_horizontal = len(set(z for _, _, z in bricks)) == 1
        if is_horizontal:
            z = bricks[0][2]
            for x, y in zip([b[0] for b in bricks], [b[1] for b in bricks]):
                if z - 1 <= 0 or (x, y, z - 1) in blocks:
                    break
            else:
                for b in bricks:
                    del blocks[b]
                    blocks[(b[0], b[1], b[2] - 1)] = id
                settled = False
        else:
            assert len(set(x for _, x, _ in bricks)) == 1
            assert len(set(y for _, y, _ in bricks)) == 1
            x = bricks[0][0]
            y = bricks[0][1]
            z = min(z for _, _, z in bricks)
            if z - 1 > 0 and (x, y, z - 1) not in blocks:
                for b in sorted(bricks, key=lambda b: b[2]):
                    del blocks[b]
                    blocks[(x, y, b[2] - 1)] = id
                settled = False


# print()
# plot_xz(blocks)
# print()
# plot_yz(blocks)


SUPPORTS = {}
ids = set(blocks.values())
for id in ids:
    bricks = [k for k, v in blocks.items() if v == id]
    supporting = set()
    for x, y, z in bricks:
        if (x, y, z + 1) in blocks:
            supporting.add(blocks[(x, y, z + 1)])
    SUPPORTS[id] = supporting - set([id])

disintegratable = set()
for id, supporting in SUPPORTS.items():
    if len(supporting) == 0:
        disintegratable.add(id)
    other_supporting = set(x for oi in ids - set([id]) for x in SUPPORTS[oi])
    if supporting.issubset(other_supporting):
        disintegratable.add(id)

print("part1", len(disintegratable))