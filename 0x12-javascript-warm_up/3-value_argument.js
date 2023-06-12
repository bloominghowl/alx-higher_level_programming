#!/usr/bin/node

const [_, __, firstArgument] = process.argv;

if (!firstArgument) {
  console.log("No argument");
} else {
  console.log(firstArgument);
}
