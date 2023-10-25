#!/usr/bin/node
// Script to display the status code of a GET request.
const request = require('request');
const urlpath = process.argv[2];
request.get(urlpath, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
