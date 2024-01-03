#!/usr/bin/node
// Writes a string to a file

const fs = require('fs');
const [, , filePath, content] = process.argv;

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Content has been written to ${filePath}`);
  }
});
