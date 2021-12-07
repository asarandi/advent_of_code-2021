#!/usr/bin/env node

import { readFileSync } from "fs";

const getInputs = (filename) => {
  const data = readFileSync(filename, "utf-8").trim().split("\n\n");
  const numbers = data[0].split(",").map((s) => parseInt(s));
  const boards = data.slice(1).map((board) =>
    board.split("\n").map((line) =>
      line
        .split(" ")
        .filter((num) => num)
        .map((num) => parseInt(num))
    )
  );
  return { numbers, boards };
};

const isWinner = (board, called) => {
  for (let i = 0; i < 5; i++) {
    let [row, col] = [true, true];
    for (let j = 0; j < 5; j++) {
      row &= board[i][j] in called;
      col &= board[j][i] in called;
    }
    if (row || col) return true;
  }
  return false;
};

const calc = (num, board, called) => {
  let res = 0;
  board.forEach((row) => {
    row.forEach((col) => {
      res += col in called ? 0 : col;
    });
  });
  return res * num;
};

const search = (numbers, boards, winnerNum) => {
  const called = {};
  const winners = {};
  for (const num of numbers) {
    called[num] = true;
    for (let i = 0; i < boards.length; i++) {
      if (i in winners) continue;
      if (!isWinner(boards[i], called)) continue;
      winners[i] = true;
      if (Object.keys(winners).length === winnerNum)
        return calc(num, boards[i], called);
    }
  }
  return -1;
};

const { numbers, boards } = getInputs("input.txt");
console.log("part 1:", search(numbers, boards, 1));
console.log("part 2:", search(numbers, boards, boards.length));
