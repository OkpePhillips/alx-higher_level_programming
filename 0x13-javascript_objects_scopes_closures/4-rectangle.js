#!/usr/bin/node
// Rectangle class with instance attributes
module.exports = class Rectangle {
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

  rotate () {
    const x = this.height;
    this.height = this.width;
    this.width = x;
    console.log(`${this.height}`);
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
