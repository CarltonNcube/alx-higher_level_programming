#!/usr/bin/node

// Import the 'list' array from the specified module ('./100-data.js')
const list = require('./100-data.js').list;

// Log the original 'list' array
console.log(list);

// Use the map function to create a new array based on the original 'list'
// Multiply each element by its index and log the result
console.log(list.map((item, index) => item * index));
