#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
fs.readFile(filepath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
