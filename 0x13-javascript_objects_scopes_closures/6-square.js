#!/usr/bin/node

const Squares = require('./5-square');

class Square extends Squares {
  constructor (size) {
    // super(size);
    this.size = size;
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
}

module.exports = Square;
