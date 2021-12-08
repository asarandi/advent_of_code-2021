#!/usr/bin/env python3

with open("input.txt") as fp:
    data = fp.read().splitlines()
    fp.close()


def is_match(candidate: str, config: tuple, known: {}) -> bool:
    digit, num_chars, compare, ref, num_shared = config
    if candidate in known.values():
        return False
    if not len(candidate) == num_chars:
        return False
    if not compare:
        return True
    return len(set(list(candidate)) & set(list(known[ref]))) == num_shared


search = [
    (8, 7, False, 0, 0),
    (7, 3, False, 0, 0),
    (1, 2, False, 0, 0),
    (4, 4, False, 0, 0),
    (2, 5, True, 4, 2),
    (3, 5, True, 2, 4),
    (5, 5, True, 3, 4),
    (9, 6, True, 3, 5),
    (6, 6, True, 5, 5),
    (0, 6, True, 8, 6),
]

p1, p2 = 0, 0
for line in data:
    left, right = line.split(" | ")
    known = {}
    for config in search:
        digit, num_chars, compare, ref, num_shared = config
        found = False
        for item in left.split(" "):
            if is_match(item, config, known):
                known[digit] = item
                found = True
                break
        assert found == True
    ct = 0
    for item in right.split(" "):
        if len(item) in [2, 3, 4, 7]:
            p1 += 1
        found = False
        for k, v in known.items():
            if set(list(item)) == set(list(v)):
                found = True
                ct = ct * 10 + k
                break
        assert found == True
    p2 += ct

print("part 1:", p1)
print("part 2:", p2)
