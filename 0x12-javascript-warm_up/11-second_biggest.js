#!/usr/bin/node

function secondMax(array) {
  array.sort();
  return array[array.length - 2];
}

const arg = process.argv;

if (arg.length <= 3) {
  console.log(0);
} else {
  const array = arg.slice(2);
  console.log(secondMax(array));
}
