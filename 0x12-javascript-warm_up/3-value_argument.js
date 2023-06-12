#!/usr/bin/node

const [_, __, firstArgument] = process.argv;

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
