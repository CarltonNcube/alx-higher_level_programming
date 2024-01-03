#!/usr/bin/node
// Prints all characters of a Star Wars movie based on Movie ID

const request = require('request');
const [, , movieId] = process.argv;
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    // Fetch and print the name of each character
    characters.forEach((characterUrl) => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const charData = JSON.parse(charBody);
          console.log(charData.name);
        }
      });
    });
  }
});
