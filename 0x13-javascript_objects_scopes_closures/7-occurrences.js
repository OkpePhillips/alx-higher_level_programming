#!/usr/bin/node
// Script to get number of occurences in a list
exports.nbOccurences = function (list, searchElement) {
  let result = 0;
  for (const item of list) {
    if (item === searchElement) {
      result++;
    }
  }
  return result;
};
