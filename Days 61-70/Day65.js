// 7kyu on CodeWars: https://www.codewars.com/kata/5949481f86420f59480000e7/train/javascript

// Given a list of numbers, determine whether the sum of its elements is odd or even.
//
// Give your answer as a string matching "odd" or "even".
//
// If the input array is empty consider it as: [0] (array with a zero).
//
// Example:
// odd_or_even([0])          ==  "even"
// odd_or_even([0, 1, 4])    ==  "odd"
// odd_or_even([0, -1, -5])  ==  "even"
// Have fun!

function oddOrEven(array) {
    let sum = 0;
    //cycle through the array
    for (let i = 0; i < array.length; i++) {
        sum += array[i];
    }
    console.log(sum);
    if (sum % 2 === 0){
        return 'even'
    }
    return 'odd'
}


oddOrEven([1023, 1, 3]); // odd
// oddOrEven([1023, 1, 2]); // even
