def part1(readings):
    predictions = []
    for reading in readings:
        seq = reading
        h = [seq]
        while not all([x == 0 for x in seq]):
            seq = [b - a for a, b in zip(seq, seq[1:])]
            h.append(seq)
        h[-1].append(0)
        i = len(h) - 2
        while i >= 0:
            h[i].append(h[i][-1] + h[i + 1][-1])
            i -= 1
        predictions.append(h[0][-1])
    return sum(predictions)


def part2(readings):
    predictions = []
    for reading in readings:
        seq = reading
        h = [seq]
        while not all([x == 0 for x in seq]):
            seq = [b - a for a, b in zip(seq, seq[1:])]
            h.append(seq)
        h[-1].insert(0, 0)
        i = len(h) - 2
        while i >= 0:
            h[i].insert(0, h[i][0] - h[i + 1][0])
            i -= 1
        predictions.append(h[0][0])
    return sum(predictions)


readings = [[int(x) for x in h.split()] for h in open("in").readlines()]

print("part1", part1(readings))
print("part2", part2(readings))
