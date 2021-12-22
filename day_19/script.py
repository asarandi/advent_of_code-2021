#!/usr/bin/env python3

import math
from collections import Counter
from itertools import combinations, permutations

with open("input.txt") as fp:
    data = fp.read().strip().split("\n\n")
    fp.close()

scanners = []
for rows in data:
    beacons = []
    for line in rows.split("\n")[1:]:
        beacons.append(tuple(list(map(int, line.split(",")))))
    scanners.append(beacons)


def distance(a: tuple, b: tuple) -> int:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

# for each scanner measure distances between its beacons
# array of nested dict => [{p1: {p2: 5, p3: 7, ...}, p2: {...} }, {} ... ]
distances = []
for scanner in scanners:
    dist = {}
    for a in scanner:
        dist[a] = {}
        for b in scanner:
            if a == b:
                continue
            dist[a][b] = distance(a, b)
    distances.append(dist)

pairs = {}
for i, s0 in enumerate(distances):
    for j, s1 in enumerate(distances):
        if i == j:
            continue
        best_count = 0
        best_0, best_1 = None, None
        for k0 in s0.keys():
            for k1 in s1.keys():
                d0 = set(s0[k0].values())
                d1 = set(s1[k1].values())
                ct = len(d0 & d1)
                if ct > best_count:
                    best_count = ct
                    best_0 = k0
                    best_1 = k1
        if best_count == 0:
            continue
        d0 = set(s0[best_0].values())
        d1 = set(s1[best_1].values())
        if len(d0 & d1) < 10:
            continue
        if (j, i) in pairs:
            continue
        pairs[(i, j)] = (best_0, best_1, d0 & d1)

perm_config = []
for r in range(4):
    for comb in combinations([0, 1, 2], r):
        arr = [1, 2, 3]
        for index in comb:
            arr[index] = -arr[index]
        for perm in permutations(tuple(arr)):
            perm_config.append(perm)


def apply_perm(vec3: tuple, perm: tuple) -> tuple:
    res = []
    for index in perm:
        i = abs(index) - 1
        res.append(vec3[i] if index > 0 else -vec3[i])
    return tuple(res)


def tuple_add(a: tuple, b: tuple) -> tuple:
    return (a[0] + b[0]), (a[1] + b[1]), (a[2] + b[2])


def find_value(d: {}, val: int) -> tuple:
    for k, v in d.items():
        if v == val:
            return k
    return None


def get_relative(pair: tuple, rev: bool) -> (tuple, tuple):
    scan0, scan1 = pair
    src0, src1, shared_distances = pairs[pair]
    # scan1 position relative to scan0
    for perm in perm_config:
        candidate = apply_perm(src0 if rev else src1, perm)
        candidate = tuple_add(src1 if rev else src0, candidate)
        found = True
        for dist in shared_distances:
            # src,dst pairs
            dst0 = find_value(distances[scan0][src0], dist)
            dst1 = find_value(distances[scan1][src1], dist)
            dist0 = distance(candidate, dst1 if rev else dst0)
            dist1 = distance((0, 0, 0), dst0 if rev else dst1)
            found &= dist0 == dist1
        if found:
            return perm, candidate
    return None, None


def negative(t: tuple) -> tuple:
    return tuple(list(map(lambda i: -i, t)))


def apply_transform(beacons: [tuple], perm: tuple, offset: tuple) -> [tuple]:
    return list(
        map(lambda t: tuple_add(apply_perm(t, negative(perm)), offset), beacons)
    )


from_to = {}
to_from = {}
for (src, dst) in pairs.keys():
    from_to[src] = {} if src not in from_to else from_to[src]
    from_to[src][dst] = True

    to_from[dst] = {} if dst not in to_from else to_from[dst]
    to_from[dst][src] = True


def get_path(i: int) -> [tuple]:
    queue = [i]
    parent, seen = {i: None}, {}

    while queue:
        curr = queue.pop(0)
        if curr in seen:
            continue
        seen[curr] = True
        if curr == 0:
            path = [0]
            while True:
                p = parent[curr]
                if p == None:
                    break
                path.append(p)
                curr = p
            return path
        neigh = []
        if curr in from_to:
            neigh += from_to[curr].keys()
        if curr in to_from:
            neigh += to_from[curr].keys()
        for n in neigh:
            if n in seen:
                continue
            queue.append(n)
            parent[n] = curr
    return None


def manhattan(a: tuple, b: tuple) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


offsets = []
for index in range(len(scanners)):
    offsets.append([(0, 0, 0)])
    path = get_path(index)
    while len(path) > 1:
        left, right = path[-2], path[-1]
        if (left, right) in pairs:
            perm, offset = get_relative((left, right), False)
        if (right, left) in pairs:
            perm, offset = get_relative((right, left), True)
        scanners[index] = apply_transform(scanners[index], perm, offset)
        offsets[index] = apply_transform(offsets[index], perm, offset)
        path.pop(-1)

unique = set()
for scanner in scanners:
    for beacon in scanner:
        unique.add(beacon)
print("part 1:", len(unique))

best = 0
for c in combinations(offsets, 2):
    d = manhattan(c[0][0], c[1][0])
    best = d if d > best else best
print("part 2:", best)
