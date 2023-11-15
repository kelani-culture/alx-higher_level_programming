#!/usr/bin/node

const dict = require('./101-data').dict;

function reformatDict (dict) {
  const newObject = {};

  for (const key in dict) {
    const value = dict[key];

    if (newObject[value] === undefined) {
      newObject[value] = [key];
    } else {
      if (!Array.isArray(newObject[value])) {
        newObject[value] = [newObject[value]];
      }
      newObject[value].push(key);
    }
  }
  console.log(newObject);
}

reformatDict(dict);
