#!/usr/bin/env python3

import functools

ct = 0
dice = 0


def roll() -> int:
    global ct, dice
    res = dice + 1
    dice = dice + 1 % 100
    ct += 1
    return res


def part1(p1, s1, p2, s2) -> int:
    global ct
    if s1 > 999:
        return ct * s2
    elif s2 > 999:
        return ct * s1
    r = roll() + roll() + roll()
    p1 = (p1 + r) % 10
    s1 = s1 + p1 + 1
    return part1(p2, s2, p1, s1)


@functools.lru_cache(maxsize=None)
def part2(p1, s1, p2, s2) -> (int, int):
    if s1 > 20:
        return 1, 0
    elif s2 > 20:
        return 0, 1
    w1, w2 = 0, 0
    r = [i + j + k + 3 for i in range(3) for j in range(3) for k in range(3)]
    for rr in r:
        px = (p1 + rr) % 10
        sx = s1 + px + 1
        v2, v1 = part2(p2, s2, px, sx)
        w1, w2 = w1 + v1, w2 + v2
    return w1, w2


p1 = 6 - 1
p2 = 7 - 1

print("part 1:", part1(p1, 0, p2, 0))
print("part 2:", max(part2(p1, 0, p2, 0)))
