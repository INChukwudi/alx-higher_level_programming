#!/usr/bin/node

// script that prints a prompt if the first argument can be converted to an integer
const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
