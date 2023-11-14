#!/usr/bin/node
// initialize a variable to count the number of arguments already printed

let count = 0;

exports.logMe = function (item) {
  // print the count and the item
  console.log(`${count}: ${item}`);
  // increment the count
  count++;
};
