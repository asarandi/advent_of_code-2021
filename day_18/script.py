#!/usr/bin/env python3

import math


def get_inputs(filename: str) -> [str]:
    with open(filename) as fp:
        data = fp.read().splitlines()
        fp.close()
    return data


def magnitude(arr: [int]) -> int:
    if isinstance(arr, int):
        return arr
    return magnitude(arr[0]) * 3 + magnitude(arr[1]) * 2


def split(arr: [int]) -> ([int], bool):
    s = str(arr)
    for i in range(len(s)):
        if s[i].isdigit():
            j = i
            while s[j].isdigit():
                j += 1
            n = int(s[i:j])
            if n < 10:
                continue
            mid = [math.floor(n / 2), math.ceil(n / 2)]
            return eval(s[:i] + str(mid) + s[j:]), True
    return arr, False


def addnums(s: str, n: int, rev: bool) -> str:
    for i in range(len(s)):
        if s[i].isdigit():
            j = i
            while s[j].isdigit():
                j += 1
            m = s[i:j]
            m = m[::-1] if rev else m
            mid = str(n + int(m))
            mid = mid[::-1] if rev else mid
            return s[:i] + mid + s[j:]
    return s


def explode(arr: [int]) -> ([int], bool):
    s = str(arr)
    braces = 0
    for i in range(len(s)):
        if s[i] == "[":
            braces += 1
        elif s[i] == "]":
            braces -= 1
        else:
            continue
        if braces == 5:
            j = i + s[i:].index("]") + 1
            sub = eval(s[i:j])
            left, right = s[:i][::-1], s[j:]
            left = addnums(left, sub[0], True)
            right = addnums(right, sub[1], False)
            return eval(left[::-1] + "0" + right), True
    return arr, False


def reduce(arr: [int]) -> [int]:
    while True:
        arr, ok = explode(arr)
        if ok:
            continue
        arr, ok = split(arr)
        if not ok:
            return arr


data = get_inputs("input.txt")
arr = eval(data[0])
for line in data[1:]:
    arr = reduce([arr, eval(line)])

print("part 1:", magnitude(arr))

part2 = 0
for i in range(len(data)):
    for j in range(len(data)):
        if i == j:
            continue
        n = magnitude(reduce([eval(data[i]), eval(data[j])]))
        part2 = n if n > part2 else part2

print("part 2:", part2)
