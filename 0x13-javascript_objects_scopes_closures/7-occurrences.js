#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter(count => count === searchElement).length;
};
