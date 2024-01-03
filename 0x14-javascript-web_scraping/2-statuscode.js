#!/usr/bin/node
// Displays the status code of a GET request

const request = require('request');
const [, , url] = process.argv;

request.get(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
