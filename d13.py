grids = [[list(x) for x in g.splitlines()] for g in open("in").read().split("\n\n")]


def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        above = above[: len(below)]
        below = below[: len(above)]

        if above == below:
            return r

    return 0


def find_mirror_with_smudge(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        above = above[: len(below)]
        below = below[: len(above)]

        smudges = []
        for ri in range(0, len(above)):
            for ci in range(0, len(above[ri])):
                if above[ri][ci] != below[ri][ci]:
                    smudges.append((ri, ci))

        if len(smudges) == 1:
            return r

    return 0


def part1():
    total = 0

    for grid in grids:
        row = find_mirror(grid)
        total += row * 100

        col = find_mirror(list([list(x) for x in zip(*grid)]))
        total += col

    return total


def part2():
    total = 0

    for grid in grids:
        row = find_mirror_with_smudge(grid)
        total += row * 100

        col = find_mirror_with_smudge(list([list(x) for x in zip(*grid)]))
        total += col

    return total


print("part1", part1())
print("part2", part2())
