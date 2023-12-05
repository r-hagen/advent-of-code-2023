sections = open("in").read().split("\n\n")


def part1(sections):
    seeds = list(map(int, sections[0].split()[1:]))

    for section in sections[1:]:
        ranges = [list(map(int, line.split())) for line in section.splitlines()[1:]]
        mapped = []
        for seed in seeds:
            for drs, srs, rl in ranges:
                if srs <= seed <= srs + rl:
                    mapped.append(seed - srs + drs)
                    break
            else:
                mapped.append(seed)
        seeds = mapped

    return min(seeds)


def part2(sections):
    input = list(map(int, sections[0].split()[1:]))

    seeds = []
    for i in range(0, len(input), 2):
        seeds.append((input[i], input[i] + input[i + 1]))

    for section in sections[1:]:
        ranges = [list(map(int, line.split())) for line in section.splitlines()[1:]]
        mapped = []
        while len(seeds) > 0:
            s, e = seeds.pop()
            for drs, srs, rl in ranges:
                overlap_start = max(s, srs)
                overlap_end = min(e, srs + rl)
                if overlap_start < overlap_end:
                    mapped.append((overlap_start - srs + drs, overlap_end - srs + drs))
                    if overlap_start > s:
                        seeds.append((s, overlap_start))
                    if e > overlap_end:
                        seeds.append((overlap_end, e))
                    break
            else:
                mapped.append((s, e))
        seeds = mapped

    return min(seeds)[0]


print("part1", part1(sections))
print("part2", part2(sections))
