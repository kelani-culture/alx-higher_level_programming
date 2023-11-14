#!/usr/bin/node

class Rectangle {
  constructor (w = 0, h = 0) {
    if (w <= 0 || h <= 0) {
      return undefined;
    }
    this.width = w;
    this.height = h;
  }
  print() {
    let i, j;
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}


module.exports = Rectangle;
