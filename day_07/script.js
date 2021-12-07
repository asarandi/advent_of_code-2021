#!/usr/bin/env node

import { readFileSync } from "fs";

const getInputs = (filename) => {
  const data = readFileSync(filename, "utf-8").trim();
  return data.split(",").map((i) => parseInt(i));
};

const solve = (arr, f) => {
  const lo = Math.min(...arr);
  const hi = Math.max(...arr);
  const ct = {};
  for (let i = lo; i < hi; i++) {
    ct[i] = 0;
    arr.forEach((j) => {
      ct[i] += f(Math.abs(i - j));
    });
  }
  return Math.min(...Object.values(ct));
};

const arr = getInputs("input.txt");
console.log(
  "part 1:",
  solve(arr, (n) => n)
);
console.log(
  "part 2:",
  solve(arr, (n) => (n * (n + 1)) / 2)
);
