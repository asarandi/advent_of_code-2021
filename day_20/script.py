#!/usr/bin/env python3


def get_inputs(filename: str) -> ({}, {}, int, int):
    with open(filename) as fp:
        data = fp.read().strip()
        fp.close()

    enh, data = data.split("\n\n")
    algo = {}
    for i in range(512):
        algo[i] = 1 if enh[i] == "#" else 0

    data = data.split("\n")
    N, M = len(data), len(data[0])
    image = {}
    for y in range(N):
        for x in range(M):
            image[(y, x)] = 1 if data[y][x] == "#" else 0
    return algo, image, N, M


def solve(algo: {}, image: {}, N: int, M: int) -> (int, int):
    P, Q = 101, 50

    def count(image: {}) -> int:
        res = 0
        for py in range(-Q, N + Q + 1):
            for px in range(-Q, M + Q + 1):
                pair = (py, px)
                res = res + 1 if pair in image and image[pair] == 1 else res
        return res

    p1, p2 = 0, 0
    for index in range(51):
        p1 = count(image) if index == 2 else p1
        p2 = count(image) if index == 50 else p2
        new_image = {}
        for py in range(-P, N + P + 1):
            for px in range(-P, M + P + 1):
                val = 0
                for (sy, sx) in [(i, j) for i in range(-1, 2) for j in range(-1, 2)]:
                    pair = (sy + py, sx + px)
                    new_image[pair] = 0 if pair not in new_image else new_image[pair]
                    n = 1 if pair in image and image[pair] == 1 else 0
                    val = val << 1 | n
                new_image[(py, px)] = algo[val]
        image = new_image
    return p1, p2


p1, p2 = solve(*get_inputs("input.txt"))
print("part 1:", p1)
print("part 2:", p2)

#assert p1 == 5425
#assert p2 == 14052
# TODO: more generic solution
