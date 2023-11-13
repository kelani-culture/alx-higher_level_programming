#!/usr/bin/node

function findMax (array) {
  let max = array[0];
  let i;
  for (i = 0; i < array.length; i++) {
    if (array[i] > max) {
      max = array[i];
    }
  }
  return max;
}

const arg = process.argv;

if (arg.length <= 3) {
  console.log(0);
} else {
  const array = arg.slice(2);
  console.log(findMax(array));
}
