#!/usr/bin/node
// Setting list tags using jquery
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    const list = $('#list_movies');
    for (let i = 0; i < movies.length; i++) {
      const title = movies[i].title;
      list.append('<li>' + title + '</li>');
    }
  });
});
