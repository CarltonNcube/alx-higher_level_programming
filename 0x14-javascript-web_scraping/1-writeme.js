#!/usr/bin/node
// Writes a string to a file

const fs = require('fs');
const [, , filePath, content] = process.argv;

fs.writeFile(filePath, content, 'utf8', (err) => {
  console.log(err ? err : `The file ${filePath} has been saved!`);
});
