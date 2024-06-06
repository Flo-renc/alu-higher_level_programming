#!/usr/bin/node

// Get the first argument from the command line and convert it to an integer
const arg = parseInt(process.argv[2]);

// Recursive function to compute the factorial
const factorial = (n) => {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
};

// Compute and print the factorial
console.log(factorial(arg));
