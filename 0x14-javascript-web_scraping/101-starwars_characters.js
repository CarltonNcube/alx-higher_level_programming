#!/usr/bin/node
// This script prints all characters of a Star Wars movie 

const request = require('request');
const BASE_URL = 'https://swapi.dev/api/';
const movieID = process.argv[2];

if (movieID < 1 || movieID > 6) {
  console.error('Invalid movie ID. Please enter a number between 1 and 6.');
  process.exit(1);
}

const movieURL = BASE_URL + 'films/' + movieID;

request(movieURL, function (error, response, body) {
  if (error) {
    console.error('An error occurred:', error);
    process.exit(1);
  }
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  function printCharacterName(characterURL) {
    request(characterURL, function (error, response, body) {
      if (error) {
        console.error('An error occurred:', error);
        process.exit(1);
      }
      const characterData = JSON.parse(body);
      const name = characterData.name;
      console.log(name);
    });
  }

  for (let i = 0; i < characters.length; i++) {
    printCharacterName(characters[i]);
  }
});
