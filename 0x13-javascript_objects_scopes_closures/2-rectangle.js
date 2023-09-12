#!/usr/bin/node
// Rectangle class with instance attributes
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      Return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
