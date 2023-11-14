#!/usr/bin/node
// import dict from the file 101-data.js
const dict = require('./101-data').dict;
// create an empty object for the new dictionary
const newDict = {};
// loop through the keys of dict
for (const key in dict) {
  // get the value of the current key
  const value = dict[key];
  // check if the value is already a key in the new dictionary
  if (newDict[value]) {
    // push the current key to the list of user ids
    newDict[value].push(key);
  } else {
    // create a new list with the current key as the first element
    newDict[value] = [key];
  }
}
// print the new dictionary
console.log(newDict);
