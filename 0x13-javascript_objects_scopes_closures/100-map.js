#!/usr/bin/node

const list = require('./100-data').list;
let count = 0;
console.log(list);
const newA = list.map((num) => num * count++);
console.log(newA);
