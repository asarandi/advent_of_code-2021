#!/usr/bin/env node

import { readFileSync } from "fs";

const lines = readFileSync("input.txt", { encoding: "utf-8" })
  .trim()
  .split("\n");

const N = lines[0].length;
const getbit = (arr, i) => {
  let lo = 0;
  let hi = 0;
  arr.forEach((line) => {
    if (line[i] === "1") {
      hi++;
    } else {
      lo++;
    }
  });
  return lo <= hi ? 0 : 1;
};

let arr1 = Array.from(lines);
let arr2 = Array.from(lines);
let res = ["", "", "", ""];
for (let i = 0; i < N; i++) {
  let bit = getbit(lines, i);
  res[0] += bit.toString();
  res[1] += (bit ^ 1).toString();

  bit = getbit(arr1, i);
  if (arr1.length > 1) {
    arr1 = arr1.filter((s) => s[i] === bit.toString());
  }
  if (arr1.length === 1) {
    res[2] = arr1[0];
  }

  bit = getbit(arr2, i) ^ 1;
  if (arr2.length > 1) {
    arr2 = arr2.filter((s) => s[i] === bit.toString());
  }
  if (arr2.length === 1) {
    res[3] = arr2[0];
  }
}

res = res.map((s) => parseInt(s, 2));
console.log("part 1:", res[0] * res[1]);
console.log("part 2:", res[2] * res[3]);
