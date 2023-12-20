from collections import deque


def init():
    configuration = {}
    flipflops = {}
    conjunctions = {}

    for line in open("in").read().splitlines():
        module, receivers = line.split(" -> ")
        receivers = receivers.split(", ")
        if module == "broadcaster":
            configuration[module] = receivers
        elif "%" in module:
            configuration[module[1:]] = receivers
            flipflops[module[1:]] = 0
        elif "&" in module:
            configuration[module[1:]] = receivers
            conjunctions[module[1:]] = {}

    for conjunction in conjunctions.keys():
        for module, receivers in configuration.items():
            if conjunction in receivers:
                conjunctions[conjunction][module] = 0

    return (configuration, flipflops, conjunctions)


def aptly(CFG, FFS, CON):
    low = 0
    high = 0
    rx = False

    q = deque()
    q.append((None, "broadcaster", 0))
    while q:
        sender, module, signal = q.popleft()

        if signal == 1:
            high += 1
        else:
            low += 1

        if module == "broadcaster":
            for receiver in CFG[module]:
                q.append((sender, receiver, signal))
        elif module in FFS and signal == 0:
            FFS[module] ^= 1
            for receiver in CFG[module]:
                q.append((module, receiver, FFS[module]))
        elif module in CON:
            CON[module][sender] = signal
            all_high = all([True if s == 1 else False for s in CON[module].values()])
            for receiver in CFG[module]:
                q.append((module, receiver, 0 if all_high else 1))
        elif module == "rx" and signal == 0:
            rx = True
        # elif module == "output":
        #     print("output", signal)

    return (low, high, rx)


def part1():
    CFG, FFS, CON = init()
    low, high = (0, 0)
    for _ in range(1000):
        l, h, _ = aptly(CFG, FFS, CON)
        low += l
        high += h
    return low * high


def part2():
    CFG, FFS, CON = init()

    # TODO: find a way to calculate the button presses without brute force
    seen = set()
    q = deque(["rx"])
    while q:
        x = q.popleft()

        if x in seen:
            continue
        seen.add(x)

        modules = [module for module, receivers in CFG.items() if x in receivers]
        print(x, modules)

        for module, receivers in CFG.items():
            if x in receivers:
                q.append(module)

    print(q)
    print("conjunctions", [x for x in seen if x in CON.keys()])
    print("flipflops", [x for x in seen if x in FFS.keys()])
    exit(0)

    # NOTE: brute force wont work here
    count = 1
    while True:
        rx = aptly(CFG, FFS, CON)[2]
        if rx:
            return count
        if count % 100_000 == 0:
            print(count)
        count += 1


print("part1", part1())
print("part2", part2())
