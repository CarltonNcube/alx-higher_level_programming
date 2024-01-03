#!/usr/bin/node
// Reads and prints the content of a file

const fs = require('fs');
const [, , filePath] = process.argv;

fs.readFile(filePath, 'utf8', (err, data) => {
  console.log(err ? err : data);
});
