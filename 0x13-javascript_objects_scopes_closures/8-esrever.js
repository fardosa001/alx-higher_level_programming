#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];

  for (let j = list.length - 1; j >= 0; j--) {
    revList.push(list[j]);
  }
  return revList;
};
