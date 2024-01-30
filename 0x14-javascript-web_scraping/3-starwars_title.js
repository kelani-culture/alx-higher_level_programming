#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get({ url, json: true }, (error, response, jsonData) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(jsonData.title);
});
