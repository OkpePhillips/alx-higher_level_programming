#!/usr/bin/node
// Script to print text if argument ccan be converted to number
const firstArgument = Number(process.argv[2]);
if (isNaN(firstArgument)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${firstArgument}`);
}
