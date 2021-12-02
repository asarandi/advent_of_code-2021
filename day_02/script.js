#!/usr/bin/env node

import { readFileSync } from "fs";

const lines = readFileSync("input.txt", { encoding: "utf-8" })
  .trim()
  .split("\n");

let y = 0;
let x = 0;
let z = 0;
lines.forEach((line) => {
  const cmd = line.split(" ")[0];
  const val = parseInt(line.split(" ")[1]);
  if (cmd === "forward") {
    x += val;
    z += y * val;
  } else if (cmd === "down") {
    y += val;
  } else if (cmd === "up") {
    y -= val;
  }
});

console.log("part 1:", x * y);
console.log("part 2:", x * z);
