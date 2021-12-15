#!/usr/bin/env python3

from heapq import heappush, heappop


def get_inputs(filename: str) -> ([[int]], [[int]]):
    with open(filename) as fp:
        data = fp.read().splitlines()
        fp.close()

    grid1 = []
    for line in data:
        row = [int(x) for x in list(line)]
        grid1.append(row)

    def add(i: int, n: int) -> int:
        m = i + n
        return m if m < 10 else (m % 10) + 1

    temp = []
    for row in grid1:
        temp_row = []
        for i in range(5):
            temp_row += list(map(lambda n: add(i, n), row))
        temp.append(temp_row)

    grid2 = []
    for i in range(5):
        for temp_row in temp:
            grid2.append(list(map(lambda n: add(i, n), temp_row)))

    return grid1, grid2


def solve(grid: [[int]]) -> int:
    N, M = len(grid), len(grid[0])
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
            heappush(queue, (risk + grid[sy][sx], sy, sx))
    return -1


grid1, grid2 = get_inputs("input.txt")
print("part 1:", solve(grid1))
print("part 2:", solve(grid2))
