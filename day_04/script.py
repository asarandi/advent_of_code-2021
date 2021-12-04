#!/usr/bin/env python3


def get_inputs() -> ([str], [[[str]]]):
    with open("input.txt") as fp:
        data = fp.read()
        fp.close()

    lines = data.strip().split("\n\n")
    numbers = [num for num in lines[0].split(",")]

    boards = []
    for line in lines[1:]:
        board = [[col for col in row.split()] for row in line.split("\n")]
        boards.append(board)
    return numbers, boards


def calc(num: str, board: [[str]], called: {}) -> int:
    res = 0
    for row in board:
        for col in row:
            if col not in called:
                res += int(col)
    return res * int(num)


def is_winner(board: [[str]], called: {}) -> bool:
    for i in range(5):
        row, col = True, True
        for j in range(5):
            row &= board[i][j] in called
            col &= board[j][i] in called
        if row or col:
            return True
    return False


def search(numbers: [str], boards: [[[str]]], winner_num: int) -> int:
    called = {}
    winners = {}
    for num in numbers:
        called[num] = True
        for bi, board in enumerate(boards):
            if bi in winners:
                continue
            if not is_winner(board, called):
                continue
            winners[bi] = True
            if len(winners) == winner_num:
                return calc(num, board, called)
    return -1


numbers, boards = get_inputs()
print("part 1:", search(numbers, boards, 1))
print("part 2:", search(numbers, boards, len(boards)))
