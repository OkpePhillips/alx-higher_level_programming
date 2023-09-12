#!/usr/bin/node
// Script to print the second biggest integer in the argument list
let argumentList = process.argv.slice(2);
if (argumentList.length === 0 || argumentList.length === 1) {
  console.log(0);
} else {
  argumentList = argumentList.map(Number);
  argumentList.sort(function (a, b) { return b - a; });
  const secondBiggest = argumentList[1];
  console.log(secondBiggest);
}
