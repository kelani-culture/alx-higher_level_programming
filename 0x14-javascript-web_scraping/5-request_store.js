#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const argument = process.argv.slice(2);

request.get(argument[0], (error, response, body) => {
    if (error) {
        console.log(error);
        return;
    }

}).pipe(fs.createWriteStream(argument[1]))