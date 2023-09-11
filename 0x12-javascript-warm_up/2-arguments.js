#!/usr/bin/node
// Script to print text output based on number of arguments

let count = 0;
while (typeof process.argv[count + 2] !== 'undefined') {
  count++;
}
if (count === 0) {
  console.log('No argument');
} else if (count === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
