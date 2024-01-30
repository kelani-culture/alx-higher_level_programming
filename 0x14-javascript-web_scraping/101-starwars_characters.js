#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get({ url: apiUrl, json: true }, (error, response, movieData) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  // Iterate through characters array in the same order as in the /films/ response
  movieData.characters.reduce((promise, characterUrl) => {
    return promise.then(() => {
      return new Promise((resolve) => {
        request.get(
          { url: characterUrl, json: true },
          (error, response, characterData) => {
            if (error) {
              console.error('Error fetching character data:', error);
              resolve();
              return;
            }

            console.log(characterData.name);
            resolve();
          }
        );
      });
    });
  }, Promise.resolve());
});
