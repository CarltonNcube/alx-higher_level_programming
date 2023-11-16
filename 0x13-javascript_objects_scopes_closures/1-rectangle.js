#!/usr/bin/node

// Define a Rectangle class
class Rectangle {
  // Constructor takes width (w) and height (h) as parameters
  constructor (w, h) {
    // Set the width and height as properties of the class instance
    this.width = w;
    this.height = h;
  }
}

// Export the Rectangle class to make it available for use in other files/modules
module.exports = Rectangle;
