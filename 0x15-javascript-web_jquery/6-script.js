#!/usr/bin/node
// Updating text using jquery
$(document).ready(function () {
  $('#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
