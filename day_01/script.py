#!/usr/bin/env python3

with open("input.txt") as fp:
    data = list(map(lambda i: int(i), fp.read().splitlines()))
    fp.close

ct = 0
prev = data[0]
for i in range(len(data)):
    curr = data[i]
    ct = ct + 1 if curr > prev else ct
    prev = curr

print("part 1", ct)

ct = 0
prev = sum(data[:3])
for i in range(len(data) - 2):
    curr = sum(data[i : i + 3])
    ct = ct + 1 if curr > prev else ct
    prev = curr

print("part 2", ct)
