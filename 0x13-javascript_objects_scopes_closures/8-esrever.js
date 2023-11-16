#!/usr/bin/node

exports.esrever = function (list) {
  // initialize an empty array
  const reversed = [];
  // loop through the list from the end to the beginning
  for (let i = list.length - 1; i >= 0; i--) {
    // push the current element to the reversed array
    reversed.push(list[i]);
  }
  // return the reversed array
  return reversed;
};
