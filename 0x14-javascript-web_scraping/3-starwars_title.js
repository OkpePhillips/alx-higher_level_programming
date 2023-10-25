#!/usr/bin/node
// Script to title of a Star Wars movie where the episode number matches a given integer
const request = require('request');
const id = process.argv[2];
const urlpath = `https://swapi-api.alx-tools.com/api/films/${id}`;
request.get(urlpath, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    console.log(`Title: ${film.title}`);
  }
});
