#!/usr/bin/node

const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint(c) {
    // If c is undefined, use 'X'
    c = c || 'X';

    // Validate that c is a single character
    if (typeof c !== 'string' || c.length !== 1) {
      throw new Error('Invalid character. Please provide a single character.');
    }

    // Print the square using the specified character c
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
