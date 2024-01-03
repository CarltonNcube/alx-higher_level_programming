#!/usr/bin/node
// Writes a string to a file

const fs = require('fs');
const [, , filePath, string] = process.argv;

fs.writeFile(filePath, string, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
