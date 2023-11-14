#!/usr/bin/node

const Square = require('./5-square');

class Square extends Square {
  constructor(size) {
    // call the constructor of Square
    super(size);
  }

  charPrint(c) {
    // print the square using the character c
    if (c === undefined) {
      // use the character X if c is undefined
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
