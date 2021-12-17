#!/usr/bin/env python3

import re


def get_inputs(filename: str) -> [int]:
    with open(filename) as fp:
        data = fp.read()
        fp.close()
    res = re.match(r".*x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", data).groups()
    assert len(res) == 4
    return [int(x) for x in res]


def solve(target: [int]) -> (int, int):
    part1, part2 = 0, {}
    for y in range(min(target), max(target) + 1):
        for x in range(min(target), max(target) + 1):
            vx, vy = x, y
            px, py, ymax = 0, 0, 0
            for _ in range(999):
                ymax = py if py > ymax else ymax
                if (target[0] <= px <= target[1]) and (target[2] <= py <= target[3]):
                    part1 = ymax if ymax > part1 else part1
                    part2[(y, x)] = True
                px, py = px + vx, py + vy
                vx = vx + 1 if vx < 0 else vx - 1 if vx > 0 else vx
                vy = vy - 1
    return part1, len(part2)


p1, p2 = solve(get_inputs("input.txt"))
print("part 1:", p1)
print("part 2:", p2)
