#!/usr/bin/node
// Script to print the number of arguments already printed
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
