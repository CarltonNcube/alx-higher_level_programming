#!/usr/bin/node

// Import the Rectangle class from the specified module ('./4-rectangle')
const Rectangle = require('./4-rectangle');

// Define a Square class that extends the Rectangle class
class Square extends Rectangle {
  // Constructor for the Square class, taking the 'size' parameter
  constructor (size) {
    // Call the constructor of the parent class (Rectangle) with 'size' for both width and height
    super(size, size);
  }
}

// Export the Square class to make it available for use in other files/modules
module.exports = Square;
