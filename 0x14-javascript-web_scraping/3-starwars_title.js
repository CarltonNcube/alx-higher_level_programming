#!/usr/bin/node
// Prints the title of a Star Wars movie based on the movie ID

const request = require('request');
const [, , movieId] = process.argv;
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
