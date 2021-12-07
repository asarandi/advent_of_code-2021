#!/usr/bin/env python3

from typing import Callable


def get_inputs() -> [int]:
    with open("input.txt") as fp:
        data = fp.read().splitlines()
        fp.close()
    return [int(i) for i in data[0].split(",")]


def solve(arr: [int], f: Callable[[int], int]) -> int:
    ct = {}
    for i in range(min(arr), max(arr)):
        ct[i] = 0
        for j in arr:
            ct[i] += f(abs(i - j))
    return min(ct.values())


arr = get_inputs()
print("part 1:", solve(arr, lambda n: n))
print("part 2:", solve(arr, lambda n: n * (n + 1) // 2))
