#!/usr/bin/node
// Fetching a string from an html tag
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    const string = data.hello;
    $('#hello').text(string);
  });
});
