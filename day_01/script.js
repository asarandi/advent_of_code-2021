#!/usr/bin/env node

import { openSync, readFileSync, closeSync } from "fs";

const fd = openSync("input.txt");
const str = readFileSync(fd, { encoding: "utf-8" });
closeSync(fd);
const data = str
  .trim()
  .split("\n")
  .map((i) => parseInt(i));

let ct = 0;
let prev = data[0];
data.forEach((curr) => {
  ct = curr > prev ? ct + 1 : ct;
  prev = curr;
});
console.log("part 1:", ct);

ct = 0;
prev = data.slice(0, 3).reduce((a, b) => a + b, 0);
for (let i = 0, curr; i < data.length - 2; i++) {
  curr = data.slice(i, i + 3).reduce((a, b) => a + b, 0);
  ct = curr > prev ? ct + 1 : ct;
  prev = curr;
}
console.log("part 2:", ct);
