#!/usr/bin/node
const arg = process.argv;
try {
  if (arg[2] === undefined) {
    throw new Error('No argument');
  }
  console.log(arg[2]);
} catch (error) {
  console.error(error.message);
}
