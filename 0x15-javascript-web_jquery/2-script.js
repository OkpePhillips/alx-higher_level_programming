#!/usr/bin/node
// Changing color on click using jquery
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
