#!/usr/bin/node
// Adding html tags using jquery
$(document).ready(function () {
  $('#add_item').click(function () {
    $('<li>Item</li>').appendTo('ul.my_list');
  });
});
