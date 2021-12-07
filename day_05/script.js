#!/usr/bin/env node

import { readFileSync } from "fs";

const getInputs = (filename) => {
  return readFileSync(filename, "utf-8")
    .trim()
    .split("\n")
    .map((line) =>
      line
        .replace(" -> ", ",")
        .split(",")
        .map((w) => parseInt(w))
    );
};

const solve = (arr, withDiagonals) => {
  const ct = {};
  for (let [x0, y0, x1, y1] of arr) {
    if (!(x0 == x1 || y0 == y1)) if (!withDiagonals) continue;
    const sx = x0 === x1 ? 0 : x0 < x1 ? 1 : -1;
    const sy = y0 === y1 ? 0 : y0 < y1 ? 1 : -1;
    while (!(x0 === x1 + sx && y0 === y1 + sy)) {
      const p = [x0, y0].toString();
      ct[p] = p in ct ? ct[p] + 1 : 1;
      (x0 = x0 + sx), (y0 = y0 + sy);
    }
  }
  return Object.values(ct).filter((v) => v > 1).length;
};

const data = getInputs("input.txt");
console.log("part 1:", solve(data, false));
console.log("part 2:", solve(data, true));
