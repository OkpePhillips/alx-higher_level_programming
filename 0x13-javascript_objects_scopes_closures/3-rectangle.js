#!/usr/bin/node
// Rectangle class with instance attributes
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      Rectangle;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const text = 'X';
    const rectangle = text.repeat(this.width);
    while (this.height > 0) {
      console.log(rectangle);
      this.height--;
    }
  }
}
module.exports = Rectangle;
