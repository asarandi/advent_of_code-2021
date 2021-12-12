#!/usr/bin/env python3


def get_inputs(filename: str) -> {}:
    with open(filename) as fp:
        data = fp.read().splitlines()
        fp.close()

    caves = {}
    for line in data:
        src, dst = line.split("-")
        caves[src] = {} if src not in caves else caves[src]
        caves[src][dst] = True
        caves[dst] = {} if dst not in caves else caves[dst]
        caves[dst][src] = True
    return caves


def all_unique(path: [str]) -> bool:
    seen = {}
    for p in path:
        if not p.islower():
            continue
        if p in seen:
            return False
        seen[p] = True
    return True


def solve(caves: {}, allow_dupe: bool) -> int:
    res = 0
    queue = ["start"]
    while queue:
        curr = queue.pop(0)
        path = curr.split(",")
        if path[-1] == "end":
            res += 1
            continue
        for step in caves[path[-1]]:
            if step.islower() and step in path:
                if step in ("start", "end"):
                    continue
                if not allow_dupe or not all_unique(path):
                    continue
            queue.append(f"{curr},{step}")
    return res


caves = get_inputs("input.txt")
print("part 1:", solve(caves, False))
print("part 2:", solve(caves, True))
