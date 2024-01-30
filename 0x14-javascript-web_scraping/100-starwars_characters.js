#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get({ url: apiUrl, json: true }, (error, response, movieData) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  // Display each character name
  movieData.characters.forEach((characterUrl) => {
    request.get(
      { url: characterUrl, json: true },
      (error, response, characterData) => {
        if (error) {
          console.error('Error fetching character data:', error);
          return;
        }

        console.log(characterData.name);
      }
    );
  });
});
