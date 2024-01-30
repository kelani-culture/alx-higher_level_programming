#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18; // Character ID for Wedge Antilles

// Make a request to the Star Wars API to get information about films
request.get({ url: apiUrl, json: true }, (error, response, data) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = data.results;

  // Count the number of films where Wedge Antilles is present
  const numberOfFilmsWithWedge = films.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  ).length;

  console.log(`${numberOfFilmsWithWedge}`);
});
