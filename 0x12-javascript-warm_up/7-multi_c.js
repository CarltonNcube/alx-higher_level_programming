#!/usr/bin/node

const numberOfOccurrences = parseInt(process.argv[2]);

if (isNaN(numberOfOccurrences)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numberOfOccurrences; i++) {
    console.log('C is fun');
  }
}
