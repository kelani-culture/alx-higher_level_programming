#!/usr/bin/node

const arg = process.argv;

function add(a, b) {
 try {
    if (!isNaN(a) && !isNaN(b)) {
      const a = parseInt(a)
      const b = parseInt(b);
      if (a === undefined) {
         throw new Error('NaN');
      }
    }
  }
  catch (error) {
    console.log(error.message);
  }
 }

let sum = add(arg[2], arg[3]);
console.log(sum);
