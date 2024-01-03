#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

const [, , url, filePath] = process.argv;

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(file, body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
