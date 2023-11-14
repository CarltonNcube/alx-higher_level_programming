#!/usr/bin/node

exports.converter = function (base) {
  // return a function that takes a number as an argument
  return function (num) {
    // convert the number to the given base using toString method
    return num.toString(base);
  };
};
