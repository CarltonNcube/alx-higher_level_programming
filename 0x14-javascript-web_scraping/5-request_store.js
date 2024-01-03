#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');
const [, , url, filePath] = process.argv;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(`Error fetching ${url}: ${error.message}`);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(`Error saving content to ${filePath}: ${err.message}`);
      } else {
        console.log(`The content has been saved to ${filePath}`);
      }
    });
  }
});
