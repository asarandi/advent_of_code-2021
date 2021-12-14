#!/usr/bin/env python3


def get_inputs(filename: str) -> ({}, {}):
    with open(filename) as fp:
        data = fp.read().splitlines()
        fp.close()

    line = data[0]
    polymer = {}
    for i in range(2, len(line) + 1):
        p = line[i - 2 : i]
        polymer[p] = 1 if p not in polymer else polymer[p] + 1

    pairs = {}
    for line in data[2:]:
        ab, c = line.split(" -> ")
        pairs[ab] = c
    return polymer, pairs


def delta(polymer: {}) -> int:
    ct, f = {}, True
    for k, v in polymer.items():
        a, b = k
        if f:
            ct[a], f = v, False
        ct[b] = v if b not in ct else ct[b] + v
    return max(ct.values()) - min(ct.values())


def solve(polymer: {}, pairs: {}):
    p1 = 0
    for i in range(40):
        next_gen = {}
        for k, v in polymer.items():
            (a, b), c = k, pairs[k]
            ac, cb = a + c, c + b
            next_gen[ac] = v if ac not in next_gen else next_gen[ac] + v
            next_gen[cb] = v if cb not in next_gen else next_gen[cb] + v
        polymer = next_gen
        p1 = delta(polymer) if i == 9 else p1
    return p1, delta(polymer)


p1, p2 = solve(*get_inputs("input.txt"))
print("part 1:", p1)
print("part 2:", p2)
