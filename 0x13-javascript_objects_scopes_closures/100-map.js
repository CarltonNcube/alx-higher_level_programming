#!/usr/bin/node

// Import the 'list' array from the specified module ('./100-data.js')
const list = require('./100-data.js').list;

// Log the original 'list' array
console.log("Original List:", list);

// Use the map function to create a new array based on the original 'list'
// Multiply each element by its index
const newList = list.map((item, index) => item * index);

// Log the new list
console.log("New List:", newList);
