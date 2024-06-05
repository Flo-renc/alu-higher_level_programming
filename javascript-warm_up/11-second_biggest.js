#!/usr/bin/node

// Convert command line arguments to an array of integers
const args = process.argv.slice(2).map(Number);

// Function to find the second biggest integer
function findSecondBiggest(arr) {
    if (arr.length < 2) {
        return 0;
    }
    
    let first = -Infinity;
    let second = -Infinity;
    
    for (let num of arr) {
        if (num > first) {
            second = first;
            first = num;
        } else if (num > second && num !== first) {
            second = num;
        }
    }
    
    return second;
}

// Print the result
console.log(findSecondBiggest(args));
