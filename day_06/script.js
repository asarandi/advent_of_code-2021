#!/usr/bin/env node

import { readFileSync } from "fs";

const getInputs = (filename) => {
  const ct = {};
  readFileSync(filename, "utf-8")
    .trim()
    .split(",")
    .map((s) => parseInt(s))
    .forEach((i) => {
      ct[i] = i in ct ? ct[i] + 1 : 1;
    });
  return ct;
};

const solve = (ct, days) => {
  for (; days > 0; days--) {
    let re = {};
    for (let i = 0; i <= 8; i++) {
      if (!(i in ct)) continue;
      if (i === 0) re[6] = re[8] = ct[i];
      else re[i - 1] = i - 1 in re ? re[i - 1] + ct[i] : ct[i];
    }
    ct = re;
  }
  return Object.values(ct).reduce((a, b) => a + b, 0);
};

const ct = getInputs("input.txt");
console.log("part 1:", solve(ct, 80));
console.log("part 2:", solve(ct, 256));
