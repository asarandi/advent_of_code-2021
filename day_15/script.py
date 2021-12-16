#!/usr/bin/env python3

from heapq import heappush, heappop


def get_inputs(filename: str) -> ([[int]], [[int]]):
    with open(filename) as fp:
        data = [[int(c) for c in list(r)] for r in fp.read().splitlines()]
        fp.close()
    return data


def solve(grid: [[int]], scale: int) -> int:
    n, m = len(grid), len(grid[0])
    N, M = n * scale, m * scale
    queue = [(0, 0, 0)]
    seen = {(0, 0): True}
    while queue:
        risk, y, x = heappop(queue)
        if (y, x) == (N - 1, M - 1):
            return risk
        for (sy, sx) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            sy, sx = sy + y, sx + x
            if not (0 <= sy < N and 0 <= sx < M):
                continue
            if (sy, sx) in seen:
                continue
            seen[(sy, sx)] = True
            val = grid[sy % n][sx % m] + (sy // n) + (sx // m)
            val = val if val < 10 else (val % 10) + 1
            heappush(queue, (risk + val, sy, sx))
    return -1


data = get_inputs("input.txt")
print("part 1:", solve(data, 1))
print("part 2:", solve(data, 5))
