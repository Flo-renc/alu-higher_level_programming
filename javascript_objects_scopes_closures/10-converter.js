#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    if (number < base) {
      return number.toString(base).toUpperCase();
    } else {
      return exports.converter(base)(Math.floor(number / base)) + (number % base).toString(base).toUpperCase();
    }
  };
};
