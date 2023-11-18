#!/usr/bin/node
const baseSquare = require('./5-square');

module.exports = class Square extends baseSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let s = 0; s < this.height; s++) {
      console.log(c.repeat(this.width));
    }
  }
};
