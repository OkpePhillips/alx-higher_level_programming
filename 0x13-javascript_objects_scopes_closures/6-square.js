#!/usr/bin/node
// Class Square extending the square class n 5-square.js
const ParentSquare = require('./5-square');
class Square extends ParentSquare {
  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
