#!/usr/bin/env python3


def get_inputs(filename: str) -> [str]:
    with open(filename) as fp:
        data = fp.read().splitlines()
        fp.close()
    return data


def solve(data: [str]) -> (int, int):
    braces = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scores = {")": (3, 1), "]": (57, 2), "}": (1197, 3), ">": (25137, 4)}
    p1, p2 = 0, []
    for line in data:
        closing = []
        for c in line:
            if c in braces:
                closing.append(braces[c])
            else:
                last = closing.pop(-1)
                if last == c:
                    continue
                p1 += scores[c][0]
                closing = []
                break
        if not closing:
            continue
        ct = 0
        for c in reversed(closing):
            ct = ct * 5 + scores[c][1]
        p2.append(ct)
    return p1, sorted(p2)[len(p2) // 2]


data = get_inputs("input.txt")
p1, p2 = solve(data)
print("part 1:", p1)
print("part 2:", p2)
