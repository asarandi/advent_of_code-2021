#!/usr/bin/env python3

with open("input.txt") as fp:
    data = fp.read().splitlines()
    fp.close()

y, x, z = 0, 0, 0
for line in data:
    cmd, val = line.split()
    val = int(val)
    if cmd == "forward":
        x += val
        z += y * val
    if cmd == "down":
        y += val
    if cmd == "up":
        y -= val

print("part 1:", x * y)
print("part 2:", x * z)
