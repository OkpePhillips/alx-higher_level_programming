#!/usr/bin/node
// Script to execute x times a function
exports.callMeMoby = function (x, theFunction) {
  while (x > 0) {
    theFunction();
    x--;
  }
};
