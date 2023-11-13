#!/usr/bin/node

const arg = process.argv;

if (arg.length <= 2 || isNaN(arg[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(arg[2]);
  let i = 0;
  while (i < size) {
    let j = 0;
    while (j < size) {
      process.stdout.write('X');
      j++;
    }
    process.stdout.write('\n');
    i++;
  }
}
