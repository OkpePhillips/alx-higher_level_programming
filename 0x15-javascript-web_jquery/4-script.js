#!/usr/bin/node
// Implementing toggle using jquery
$(document).ready(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
