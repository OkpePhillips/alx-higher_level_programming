#!/usr/bin/node
// A script to read and print the content of a file
const fs = require('fs');
const filePath = process.argv[2];
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
