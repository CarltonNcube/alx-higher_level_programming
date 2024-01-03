#!/usr/bin/node
// Prints all characters of a Star Wars movie based on Movie ID in the same order

const request = require('request');
const [, , movieId] = process.argv;
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    // Fetch and print the name of each character in the same order
    let charactersProcessed = 0;

    characterUrls.forEach((characterUrl, index) => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const charData = JSON.parse(charBody);
          console.log(charData.name);

          // Check if all characters are processed before printing newline
          charactersProcessed++;
          if (charactersProcessed === characterUrls.length) {
            console.log();
          }
        }
      });
    });
  }
});
