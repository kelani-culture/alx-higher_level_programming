#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

// Make a request to the JSONPlaceholder API to get information about todos
request.get({ url: apiUrl, json: true }, (error, response, todos) => {
  if (error) {
    console.error(error);
    return;
  }

  // Group todos by userId
  const completedTasksByUser = todos.reduce((result, todo) => {
    if (todo.completed) {
      result[todo.userId] = (result[todo.userId] || 0) + 1;
    }
    return result;
  }, {});

  console.log(completedTasksByUser);
});
