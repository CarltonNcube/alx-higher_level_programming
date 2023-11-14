#!/usr/bin/node
// import list from the file 100-data.js
const list = require('./100-data').list;
// print the initial list
console.log(list);
// use map to create a new list with each value multiplied by the index
console.log(list.map((value, index) => value * index));
