#!/usr/bin/env python3


def get_inputs() -> {}:
    with open("input.txt") as fp:
        data = fp.read().splitlines()
        fp.close()

    ct = {}
    for n in map(lambda i: int(i), data[0].split(",")):
        ct[n] = 1 if n not in ct else ct[n] + 1
    return ct


def solve(ct: {}, num_days: int) -> int:
    for _ in range(num_days):
        re = {}
        for i in range(8 + 1):
            if i not in ct:
                continue
            if i == 0:
                re[6] = ct[i]
                re[8] = ct[i]
            else:
                re[i - 1] = ct[i] if i - 1 not in re else re[i - 1] + ct[i]
        ct = re
    return sum(ct.values())


print("part 1:", solve(get_inputs(), 80))
print("part 2:", solve(get_inputs(), 256))
