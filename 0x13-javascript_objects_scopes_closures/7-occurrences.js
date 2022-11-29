#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((accumulator, current) => (current === searchElement) ? ++accumulator : accumulator, 0);
};
