import math

instructions, network = open("in").read().split("\n\n")

N = {}
for n in network.split("\n"):
    node, paths = n.split(" = ")
    left, right = paths.strip("()").split(", ")
    N[node] = (left, right)


def part1():
    node = "AAA"
    i = 0
    steps = 0
    while node != "ZZZ":
        node = N[node][0 if instructions[i] == "L" else 1]
        i = i + 1 if i + 1 < len(instructions) else 0
        steps += 1
    return steps


def part2():
    nodes = [node for node in N.keys() if node.endswith("A")]
    steps = []
    for node in nodes:
        i = 0
        s = 0
        while not node.endswith("Z"):
            node = N[node][0 if instructions[i] == "L" else 1]
            i = i + 1 if i + 1 < len(instructions) else 0
            s += 1
        steps.append(s)
    lcm = 1
    for i in steps:
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm


print("part1", part1())
print("part2", part2())
