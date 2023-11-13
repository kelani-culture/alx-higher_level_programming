#!/usr/bin/node

const arg = process.argv;

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

if (arg.length <= 3 || (isNaN(arg[2]) && isNaN(arg[3]))) {
  console.log(NaN);
} else {
  add(arg[2], arg[3]);
}
