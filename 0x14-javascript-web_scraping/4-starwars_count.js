#!/usr/bin/node
// Prints the number of movies where "Wedge Antilles" is present

const request = require('request');
const [, , apiUrl] = process.argv;
const characterId = '18';

request(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const films = JSON.parse(body).results || [];
    let count = 0;

    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes(`/${characterId}/`)) {
          count++;
        }
      }
    }

    console.log(count);
  } else {
    console.log('Invalid');
  }
});
