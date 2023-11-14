#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // initialize a counter variable
  let count = 0;
  // loop through the list
  for (let i = 0; i < list.length; i++) {
    // check if the current element matches the search element
    if (list[i] === searchElement) {
      // increment the counter
      count++;
    }
  }
  // return the counter
  return count;
};
