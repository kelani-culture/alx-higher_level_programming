#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18; // Character ID for Wedge Antilles

// Make a request to the Star Wars API to get information about films
request.get({ apiUrl, json: true }, (error, response, data) => {
  if (error) {
    console.log(error);
    return;
  }

  const films = data.result;
  const numberOfFilmWithWedge = films.filter((film) =>
    film.character.include(
      `https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  ).length;

  console.log(numberOfFilmWithWedge);
});
