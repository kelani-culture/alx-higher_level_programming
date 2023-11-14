#!/usr/bin/node

class Rectangle {
  constructor (w = 0, h = 0) {
    if (w <= 0 || h <= 0) {
      return undefined;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    // print rectangles in shapes
    let i, j;
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
}

module.exports = Rectangle;
