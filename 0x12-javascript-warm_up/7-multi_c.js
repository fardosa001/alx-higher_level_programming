#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (num) {
  for (let j = 0; j < num; j++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
