#!/usr/bin/env python3


def get_inputs(filename: str) -> [[int]]:
    with open(filename) as fp:
        grid = [list(map(lambda i: int(i), list(l))) for l in fp.read().splitlines()]
        fp.close()
    return grid


def solve(grid: [[int]]) -> (int, int):
    N, M = len(grid), len(grid[0])
    UDLR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_bounds(p: tuple) -> bool:
        return (0 <= p[0] < N) and (0 <= p[1] < M)

    def add_tuples(a: tuple, b: tuple) -> tuple:
        return (a[0] + b[0], a[1] + b[1])

    def bfs(start: tuple) -> int:
        queue = [start]
        seen = {}
        while len(queue) > 0:
            curr = queue.pop(0)
            seen[curr] = True
            for p in UDLR:
                step = add_tuples(curr, p)
                if step in seen:
                    continue
                if not is_bounds(step):
                    continue
                y, x = step
                if grid[y][x] == 9:
                    continue
                queue.append(step)
        return len(seen)

    p1, p2arr = 0, []
    for y in range(N):
        for x in range(M):
            val = grid[y][x]
            lowest = True
            for step in map(lambda p: add_tuples((y, x), p), UDLR):
                if not is_bounds(step):
                    continue
                i, j = step
                lowest &= val < grid[i][j]
            if lowest:
                p1 += 1 + val
                p2arr.append(bfs((y, x)))

    p2 = 1
    for n in sorted(p2arr, reverse=True)[:3]:
        p2 *= n
    return p1, p2


grid = get_inputs("input.txt")
p1, p2 = solve(grid)
print("part 1:", p1)
print("part 2:", p2)
