#!/usr/bin/node

const arg = process.argv;

if (arg.length <= 2 || isNaN(arg[2])) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(arg[2]));
}
