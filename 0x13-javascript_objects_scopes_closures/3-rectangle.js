#!/usr/bin/node
// Rectangle class with instance attributes
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return Object.create(Rectangle.prototype);
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        x += 'X';
      }
      console.log(x);
    }
  }
}
module.exports = Rectangle;
