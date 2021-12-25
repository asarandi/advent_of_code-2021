#!/usr/bin/env python3

with open("input.txt") as fp:
    data = fp.read().strip().splitlines()
    fp.close()
N = len(data)
M = len(data[0])

state = {}
for y in range(N):
    for x in range(M):
        state[(y, x)] = data[y][x]


def east(t: tuple) -> tuple:
    y, x = t
    x = (x + 1) % M
    return y, x


def south(t: tuple) -> tuple:
    y, x = t
    y = (y + 1) % N
    return y, x


def equals(a: tuple, b: tuple) -> bool:
    for y in range(N):
        for x in range(M):
            if a[(y, x)] != b[(y, x)]:
                return False
    return True


def step(state: {}) -> int:
    steps = 0
    while True:
        new_state = {}
        for k, v in state.items():
            if v != ">":
                continue
            s = east(k)
            if state[s] == ".":
                assert s not in new_state
                new_state[s] = ">"
            else:
                assert k not in new_state
                new_state[k] = ">"

        for y in range(N):
            for x in range(M):
                if (y, x) not in new_state:
                    new_state[(y, x)] = "."

        for k, v in state.items():
            if v != "v":
                continue
            s = south(k)
            if state[s] == "v":
                new_state[k] = "v"
                continue
            if new_state[s] == ".":
                new_state[s] = "v"
            else:
                new_state[k] = "v"

        steps += 1
        if equals(state, new_state):
            return steps
        state = new_state


print("part 1:", step(state))
