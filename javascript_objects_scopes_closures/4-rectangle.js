#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  double() {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }

  rotate() {
    if (this.width && this.height) {
      // Swap width and height using a temporary variable
      let temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  }
}

module.exports = Rectangle;
