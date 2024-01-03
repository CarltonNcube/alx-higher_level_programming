#!/usr/bin/node
// Prints the number of movies where the character "Wedge Antilles" is present

const request = require('request');
const [, , apiUrl] = process.argv;
const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    
    const moviesWithWedge = films.filter((film) =>
      film.characters.includes(
        `https://swapi-api.alx-tools.com/api/people/${characterId}/`
      )
    );
    
    console.log(moviesWithWedge.length);
  }
});
