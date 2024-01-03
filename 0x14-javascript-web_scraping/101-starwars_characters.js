#!/usr/bin/node
// Prints all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const film = JSON.parse(body);
    const characters = film.characters || [];

    characters.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          console.log(JSON.parse(charBody).name);
        }
      });
    });
  } catch (parseError) {
    console.error('Error parsing API response:', parseError);
  }
});

