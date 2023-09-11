#!/usr/bin/node
const arg = process.argv;
if (!isNaN(arg[2]) && arg.length > 2) {
  let num = parseInt(arg[2]);
  let i = 0;
  const sq = num;
  while (num > 0) {
    while (i < sq) {
      process.stdout.write('x');
      i += 1;
    }
    i = 0;
    num -= 1;
    console.log();
  }
} else {
  console.log('Missing size');
}
