#!/usr/bin/node
// Script to print a square using argument
let number = Number(process.argv[2]);
const text = 'X';

if (isNaN(number)) {
  console.log('Missing size');
} else {
  const square = text.repeat(number);
  while (number > 0) {
    console.log(square);
    number--;
  }
}
