#!/usr/bin/env python3

from copy import deepcopy

with open("input.txt") as fp:
    lines = fp.read().splitlines()
    fp.close()

N = len(lines[0])


def getbit(arr: [str], i: int) -> int:
    lo, hi = 0, 0
    for line in arr:
        if line[i] == "1":
            hi += 1
        else:
            lo += 1
    return 0 if lo <= hi else 1


arr1, arr2 = deepcopy(lines), deepcopy(lines)
res = ["", "", "", ""]
for i in range(N):
    bit = getbit(lines, i)
    res[0] += str(bit)
    res[1] += str(bit ^ 1)

    bit = getbit(arr1, i)
    if len(arr1) > 1:
        arr1 = list(filter(lambda s: s[i] == str(bit), arr1))
    if len(arr1) == 1:
        res[2] = arr1[0]

    bit = getbit(arr2, i) ^ 1
    if len(arr2) > 1:
        arr2 = list(filter(lambda s: s[i] == str(bit), arr2))
    if len(arr2) == 1:
        res[3] = arr2[0]

res = list(map(lambda s: int(s, 2), res))
print("part 1:", res[0] * res[1])
print("part 2:", res[2] * res[3])
