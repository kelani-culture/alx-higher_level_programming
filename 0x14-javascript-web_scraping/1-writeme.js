#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv.slice(2);

fs.writeFile(filepath[0], filepath[1], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
