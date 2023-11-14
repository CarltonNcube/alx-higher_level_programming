#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    // check if w and h are positive integers
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // create an empty object
      this.width = 0;
      this.height = 0;
    }
  }

  print() {
    // print the rectangle using X
    if (this.width > 0 && this.height > 0) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      console.log('Empty Rectangle');
    }
  }

  rotate() {
    // exchange the width and the height of the rectangle
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    // multiply the width and the height of the rectangle by 2
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;

