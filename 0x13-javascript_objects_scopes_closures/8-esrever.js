#!/usr/node/bin

exports.esrever = function(list) {
    let newList = [];
    for (element of list) {
        newList.unshift(element);
    }
    return newList;
}