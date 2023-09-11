#!/usr/bin/node
// printing text a number of times  as
// dictated by the value of argument passed to the script
let number = Number(process.argv[2]);
const text = 'C is fun';
if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  while (number > 0) {
    console.log(`${text}`);
    number--;
  }
}
