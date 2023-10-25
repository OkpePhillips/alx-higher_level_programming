#!/usr/bin/node
// Script to title of a Star Wars movie where the episode number matches a given integer
const request = require('request');
const urlpath = process.argv[2];
request.get(urlpath, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const Index in films) {
      const filmCharacters = films[Index].characters;
      for (const characterIndex in filmCharacters) {
        if (filmCharacters[characterIndex].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
