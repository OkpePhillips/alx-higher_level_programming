#!/usr/bin/node
// Adding class to header via jquery
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});
