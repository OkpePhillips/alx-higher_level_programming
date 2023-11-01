#!/usr/bin/node
// Script that fetches and prints how to say “Hello” depending on the language
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`;

    $.get(apiUrl, function (data) {
      const translation = data.hello;
      $('#hello').text(translation);
    });
  });

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      $('#btn_translate').click();
    }
  });
});
