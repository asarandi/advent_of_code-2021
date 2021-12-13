#!/usr/bin/env python3


def get_inputs(filename: str) -> ({}, [tuple]):
    with open("input.txt") as fp:
        data = fp.read().splitlines()
        fp.close()

    dots, folds = {}, []
    for line in data:
        if not line:
            continue
        if line[0] == "f":
            f, n = line.split("=")
            x, y = (int(n), 0) if f[-1] == "x" else (0, int(n))
            folds.append((x, y))
        else:
            dx, dy = [int(n) for n in line.split(",")]
            dots[(dx, dy)] = True
    return dots, folds


def solve(dots: {}, folds: [tuple]) -> (int, str):
    p1 = 0
    for fi, (fx, fy) in enumerate(folds):
        new_dots, mx, my = {}, 0, 0
        for (dx, dy) in dots:
            if fx:
                dx = fx - (dx - fx) if dx > fx else dx
            else:
                dy = fy - (dy - fy) if dy > fy else dy
            mx = dx if dx > mx else mx
            my = dy if dy > my else my
            new_dots[(dx, dy)] = True
        dots = new_dots
        p1 = len(dots) if fi == 0 else p1

    p2 = "\n"
    for y in range(my + 1):
        for x in range(mx + 1):
            p2 += "#" if (x, y) in dots else "."
        p2 += "\n"
    return p1, p2


p1, p2 = solve(*get_inputs("sample.txt"))
print("part 1:", p1)
print("part 2:", p2)
