#!/usr/bin/node

const Squares = require('./5-square');

class Square extends Squares {
//   constructor (size) {
//     // super(size);
//   }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
}

module.exports = Square;
