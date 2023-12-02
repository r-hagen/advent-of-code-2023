lines = [x.strip() for x in open("in").readlines()]


def parse_cubes(subset):
    cubes = {}
    parts = [x.strip() for x in subset.split(",")]
    for part in parts:
        count, color = part.split(" ")
        cubes[color] = int(count)
    return cubes


def parse_rounds(game):
    subsets = game.split(": ")[1].split("; ")
    return [parse_cubes(subset) for subset in subsets]


def is_game_possible(game, bag):
    for color, count in game.items():
        if color in bag:
            if count > bag[color]:
                return False
        else:
            return False
    return True


def part1(games, bag):
    result = 0
    for i, game in enumerate(games):
        rounds = parse_rounds(game)
        if all([is_game_possible(g, bag) for g in rounds]):
            result += i + 1
    return result


def part2(games):
    result = 0
    for game in games:
        rounds = parse_rounds(game)
        fewest = {}
        for g in rounds:
            for color, count in g.items():
                if color in fewest:
                    fewest[color] = max([fewest[color], count])
                else:
                    fewest[color] = count
        power = 1
        for count in fewest.values():
            power *= count
        result += power
    return result


print("part1", part1(lines, {"red": 12, "green": 13, "blue": 14}))
print("part2", part2(lines))
