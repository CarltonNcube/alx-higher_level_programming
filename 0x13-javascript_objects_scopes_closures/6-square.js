#!/usr/bin/node

// Import the SquareP class from the specified module ('./5-square')
const SquareP = require('./5-square');

// Define a Square class that extends the SquareP class
class Square extends SquareP {
  // Define a method for printing the square with a specified character
  charPrint(c) {
    // If c is undefined, use 'X'
    c = c || 'X';

    // Validate that c is a single character
    if (typeof c !== 'string' || c.length !== 1) {
      // Throw an error if the provided character is invalid
      throw new Error('Invalid character. Please provide a single character.');
    }

    // Print the square using the specified character c
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

// Export the Square class to make it available for use in other files/modules
module.exports = Square;
