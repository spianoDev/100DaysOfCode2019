// 7kyu on CodeWars: https://www.codewars.com/kata/summing-a-numbers-digits/train/javascript

// Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.
// For example:
//
// sumDigits(10);  // Returns 1
// sumDigits(99);  // Returns 18
// sumDigits(-32); // Returns 5
// Let's assume that all numbers in the input will be integer values.

function sumDigits(number) {
    let sum = 0;
    // first I will make sure the incoming number is a positive number
    let positiveNumber = Math.abs(number);
    // next I will split the number into the individual digits
    let stringNumber = positiveNumber.toString().split("");
    console.log(stringNumber);
    // now I will add the values of the new array together
    for (let i = 0; i < stringNumber.length; i++) {
        sum += Number(stringNumber[i]);
    }
    return sum;
}

console.log(sumDigits(-32));
