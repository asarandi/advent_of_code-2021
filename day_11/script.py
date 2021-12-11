#!/usr/bin/env python3


def get_inputs(filename) -> [[int]]:
    with open(filename) as fp:
        grid = [[int(x) for x in l] for l in fp.read().splitlines()]
        fp.close()
    return grid


def solve(grid: [[int]]) -> (int, int):
    steps = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    N, M = len(grid), len(grid[0])
    p1, p2 = 0, 0
    seen = {}
    while len(seen) != N * M:
        seen = {}
        for y in range(N):
            for x in range(M):
                grid[y][x] = (grid[y][x] + 1) % 10
                if grid[y][x] == 0:
                    seen[(y, x)] = True
        queue = [k for k in seen.keys()]
        while queue:
            (r, c) = queue.pop(0)
            for (y, x) in steps:
                y, x = y + r, x + c
                if not ((0 <= y < N) and (0 <= x < M)):
                    continue
                if (y, x) in seen:
                    continue
                grid[y][x] = (grid[y][x] + 1) % 10
                if grid[y][x] == 0:
                    seen[(y, x)] = True
                    queue.append((y, x))
        p2 += 1
        if p2 <= 100:
            p1 += len(seen)
    return p1, p2


p1, p2 = solve(get_inputs("input.txt"))
print("part 1:", p1)
print("part 2:", p2)
