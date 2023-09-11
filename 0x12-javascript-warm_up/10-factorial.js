#!/usr/bin/node
// Script to compute and print factorial
function factorial(num) {
  if (num === 0) {
    return 1;
    } else if (isNaN(num)) {
  return 1;
  } else {
  return (num * factorial(num - 1));
  }
}
const num = Number(process.argv[2]);
	const result = factorial(num);
	console.log(result);
