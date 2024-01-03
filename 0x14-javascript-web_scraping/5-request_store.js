#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

const [, , url, filePath] = process.argv;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
      } else {
        console.log(`The content has been saved to ${filePath}`);
      }
    });
  }
});
