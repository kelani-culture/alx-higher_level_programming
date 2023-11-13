#!/usr/bin/node

const arg = process.argv;

function fact (num) {
  if (num === 1) {
    return 1;
  }
  return num * fact(num - 1);
}
if (arg.length <= 2 || isNaN(arg[2])) {
  console.log(1);
} else {
  const int = parseInt(arg[2]);
  console.log(fact(int));
}
