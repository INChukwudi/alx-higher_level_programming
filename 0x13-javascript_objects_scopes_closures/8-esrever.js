#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight((accumulator, current) => {
    accumulator.push(current);
    return accumulator;
  }, []);
};
