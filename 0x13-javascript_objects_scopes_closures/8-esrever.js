#!/usr/node/bin

exports.esrever = function (list) {
  const newList = [];
  for (const element of list) {
    newList.unshift(element);
  }
  return newList;
};
