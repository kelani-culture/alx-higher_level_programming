#!/usr/bin/node
let arg = process.argv
if (arg.length === 4) {
  console.log(`${arg[2]} is ${arg[3]}`);
} else if (arg.length === 3) {
  console.log(`${arg[2]} is undefined`);
} else {
  console.log('undefined ' + 'is ' + 'undefined');
}
