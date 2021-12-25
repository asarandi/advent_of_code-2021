#!/usr/bin/env python3

from heapq import heappush, heappop
from copy import deepcopy


def get_inputs(filename: str) -> str:
    with open(filename) as fp:
        data = fp.read().strip()
        fp.close()
    return data


columns = {"A": 3, "B": 5, "C": 7, "D": 9}
costs = {"A": 1, "B": 10, "C": 100, "D": 1000}


hallway = [(1, 1), (1, 2), (1, 4), (1, 6), (1, 8), (1, 10), (1, 11)]
siderooms = [(2, 3), (3, 3), (2, 5), (3, 5), (2, 7), (3, 7), (2, 9), (3, 9)]


def is_path(state, y, x, Y, X) -> (bool, int):
    queue = [(y, x)]
    seen = {}
    while queue:
        pos = queue.pop(0)
        if pos[0] == Y and pos[1] == X:
            steps = 0
            while pos in seen:
                pos = seen[pos]
                steps += 1
            return True, steps
        for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            my, mx = move[0] + pos[0], move[1] + pos[1]
            if state[my][mx] != ".":
                continue
            new_pos = my, mx
            if new_pos in seen:
                continue
            seen[new_pos] = pos
            queue.append(new_pos)
    return False, 0


def clone_swap(state, y, x, Y, X) -> str:
    clone = deepcopy(state)
    clone[y][x] = state[Y][X]
    clone[Y][X] = state[y][x]
    return clone


def moves(state: str) -> (int, str):
    state = [list(l) for l in state.split("\n")]
    for src in hallway:
        sy, sx = src
        char = state[sy][sx]
        if char not in columns:
            continue
        dx = columns[char]
        for dy in range(len(state) - 2, 1, -1):
            if state[dy][dx] == char:
                continue
            if state[dy][dx] != ".":
                break
            dst = dy, dx
            ok, dist = is_path(state, *src, *dst)
            if not ok:
                break
            cost = costs[char] * dist
            clone = clone_swap(state, *src, *dst)
            s = "\n".join(["".join(l) for l in clone])
            yield cost, s
            break

    for expect, sx in columns.items():
        src, ok = None, True
        for sy in range(2, len(state) - 1):
            if state[sy][sx] == ".":
                continue
            src = (sy, sx) if src == None else src
            ok &= state[sy][sx] == expect
        if ok:
            continue
        sy, sx = src
        for dst in hallway:
            ok, dist = is_path(state, *src, *dst)
            if not ok:
                continue
            amphi = state[sy][sx]
            cost = costs[amphi] * dist
            clone = clone_swap(state, *src, *dst)
            s = "\n".join(["".join(l) for l in clone])
            yield cost, s


def search(maze: str, goal: str) -> [tuple]:
    queue = [(0, maze)]
    seen = {}
    while queue:
        node = heappop(queue)
        cost, maze = node
        if maze == goal:
            path = []
            while node in seen:
                path.append(node)
                node = seen[node]
            return path
        for child in moves(maze):
            new_cost, new_maze = child
            new_node = cost + new_cost, new_maze
            if new_node in seen:
                continue
            seen[new_node] = node
            heappush(queue, new_node)
    return [(0, "")]


def show(path: [tuple]) -> None:
    for node in reversed(path):
        cost, maze = node
        print("cost", cost)
        print(maze)
        print()


maze = get_inputs("input.txt")
goal = get_inputs("goal.txt")
path = search(maze, goal)
# show(path)
print("part 1:", path[0][0])

# input("\npress any key ...")

maze = get_inputs("input2.txt")
goal = get_inputs("goal2.txt")
path = search(maze, goal)
# show(path)
print("part 2:", path[0][0])
