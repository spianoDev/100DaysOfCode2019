// 6kyu on CodeWars: https://www.codewars.com/kata/5911385598dcd432ae000004/train/javascript

// A masked number is a string that consists of digits and one asterisk (*) that should be replaced by exactly one digit.
// Given a masked number s, find all the possible options to replace the asterisk with a digit to produce an integer divisible by 6.
//
// Input/Output
//     [input] string s
//
// A masked number.
//
// 1 ≤ inputString.length ≤ 10000.
//
//     [output] a string array
//
// Sorted array of strings representing all non-negative integers that correspond to the given mask and are divisible by 6.
//
// Example
// For s = "1*0", the output should be ["120", "150", "180"].
//
//     For s = "*1", the output should be [].
//
//     For s = "1234567890123456789012345678*0",
//
//     the output should be
//
//     [
//     "123456789012345678901234567800",
//         "123456789012345678901234567830",
//         "123456789012345678901234567860",
//         "123456789012345678901234567890"]

function isDivisibleBy6(s) {
    // find the index where the * exists
    let index = s.indexOf('*');
    console.log(index);
    // variable for number choices
    let numbers = [];
    // replace the * with a number between 0 - 9
    for (let i = 0; i <= 9; i++) {
        numbers.push(s.replace('*', i));
    }
    // see if the replaced number is divisible by 6
    console.log(numbers);
    let answer = [];
    for (let number of numbers){
        // edge case of very big numbers
        if (s.length > 20) {
            let subNum = number.substring(index, s.length);
            if (subNum % 6 === 0) {
                // answer.push(subNum); this was a test to be sure I was accessing the correct values
                answer.push(number);
            }
        } else {
            if (number % 6 === 0) {
                answer.push(number);
            }
        }
    }
    console.log(answer);
    return answer;
}

// isDivisibleBy6("1*0"); // ["120","150","180"]
// isDivisibleBy6("*"); //["0","6"]
// isDivisibleBy6("*1"); // []
// isDivisibleBy6("81234567890*"); // ["812345678904"]
isDivisibleBy6('318837704289243*5');
// isDivisibleBy6('112233445566767*126');
// isDivisibleBy6('1234567890123456789012345678*0');
// ['123456789012345678901234567800', '123456789012345678901234567830', '123456789012345678901234567860', '123456789012345678901234567890']
