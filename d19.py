def parse_workflows(lines):
    workflows = {}
    for workflow in lines:
        name, rules = workflow.split("{")
        parsed_rules = []
        for rule in rules[:-1].split(","):
            if ":" in rule:
                condition, target = rule.split(":")
                condition = condition.replace("=", "==")
                parsed_rules.append((condition, target))
            else:
                parsed_rules.append(("1==1", rule))
        workflows[name] = parsed_rules
    return workflows


def parse_parts(lines):
    parts = []
    for part in lines:
        part = part[1:-1].split(",")
        args = {}
        for p in part:
            k, v = p.split("=")
            args[k] = int(v)
        parts.append(args)
    return parts


def process(parts, workflow, workflows, accepted):
    for rule in workflows[workflow]:
        condition, target = rule
        if eval(condition, dict(parts)):
            if target == "A":
                accepted.append(parts)
                return
            elif target == "R":
                return
            else:
                process(parts, target, workflows, accepted)
                break
    else:
        raise Exception("This should not happen")


def part1(workflows, parts):
    accepted = []
    for part in parts:
        process(part, "in", workflows, accepted)
    return sum([sum(parts.values()) for parts in accepted])


top, bottom = open("in").read().split("\n\n")
workflows = parse_workflows(top.splitlines())
parts = parse_parts(bottom.splitlines())

print("part1", part1(workflows, parts))
