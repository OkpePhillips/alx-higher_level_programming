#!/usr/bin/node
// Script to add to number using a function
function add (a, b) {
  const result = Number(a) + Number(b);
  console.log(result);
}
add(process.argv[2], process.argv[3]);
