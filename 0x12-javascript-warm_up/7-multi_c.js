#!/usr/bin/node

const arg = process.argv;
if (!isNaN(arg[2])) {
  let num = parseInt(arg[2]);
  while (num > 0) {
    console.log('C is fun');
    num -= 1;
  }
}
