#!/usr/bin/node
const Square = require('./5-square.js');

class SquareWithCharPrint extends Square {
  charPrint (C) {
    if (C === undefined) {
      C = 'X';
    }
    if (this.width !== undefined && this.height !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log(C.repeat(this.width));
      }
    }
  }
}

module.exports = SquareWithCharPrint;
