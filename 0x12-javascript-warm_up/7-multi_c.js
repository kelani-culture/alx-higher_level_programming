#!/usr/bin/node

const arg = process.argv;

if (arg.length === 2) {
  console.log('Missing number of occurrences');
} else if (parseInt(arg[2] <= 0)) {
  console.log();
} else {
  let int = parseInt(arg[2]);
  while (int > 0) {
    console.log('C is fun');
    int--;
  }
}
