#!/usr/bin/env python3


def get_inputs(filename: str) -> [tuple]:
    with open(filename) as fp:
        data = fp.read().splitlines()
        fp.close()

    data = [s.replace(" -> ", ",").split(",") for s in data]
    return [tuple(map(lambda i: int(i), s)) for s in data]


def solve(arr: [tuple], with_diagonals: bool) -> int:
    ct = {}
    for (x0, y0, x1, y1) in arr:
        if not (x0 == x1 or y0 == y1):
            if not with_diagonals:
                continue
        sx = 0 if x0 == x1 else 1 if x0 < x1 else -1
        sy = 0 if y0 == y1 else 1 if y0 < y1 else -1
        while not (x0 == x1 + sx and y0 == y1 + sy):
            p = (x0, y0)
            ct[p] = 1 if p not in ct else ct[p] + 1
            x0, y0 = x0 + sx, y0 + sy
    return len(list(filter(lambda v: v > 1, ct.values())))


data = get_inputs("input.txt")
print("part 1:", solve(data, False))
print("part 2:", solve(data, True))
