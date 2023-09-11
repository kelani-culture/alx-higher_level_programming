#!/usr/bin/node
const arg = process.argv;
if (isNaN(arg[2]) || arg.length < 3) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(arg[2])}`);
}
