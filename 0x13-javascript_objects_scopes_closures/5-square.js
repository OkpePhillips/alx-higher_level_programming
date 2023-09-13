#!/usr/bin/node
// Extending Rectangle class in this script
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
