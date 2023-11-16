#!/usr/bin/node
// A class Rectangle that defines a rectangle with a constructor that
// validates the arguments

class Rectangle {
  // The constructor takes two arguments w and h
  constructor (w, h) {
    // If w or h is equal to 0 or not a positive integer, create an empty object
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return;
    }
    // Otherwise, initialize the instance attribute width with the value of w
    this.width = w;
    // And initialize the instance attribute height with the value of h
    this.height = h;
  }
}

module.exports = Rectangle;
