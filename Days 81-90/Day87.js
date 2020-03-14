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
    // console.log(index);
    // variable for number choices
    let numbers = [];
    // replace the * with a number between 0 - 9
    for (let i = 0; i <= 9; i++) {
        numbers.push(s.replace('*', i));
    }
    // see if the replaced number is divisible by 6
    // console.log(numbers);
    let answer = [];
    for (let number of numbers) {
        if (number % 6 === 0 && number.length < 23) {
            answer.push(number);
        }
        // edge case of very big numbers
        else if (number.length >= 23) {
            // if (index >= s.length - 6) {
                let subNum = number.substring(index, s.length);
                console.log(subNum);
                if (subNum % 6 === 0) {
                    // answer.push(subNum); //this was a test to be sure I was accessing the correct values
                    answer.push(number);
                // }
            // } else {
            //     let subNumBig = number.substring(index, s.length);
            //     console.log(subNumBig);
            //     if (subNumBig % 6 === 0) {
            //         answer.push(number);
            //     }
            }
        }
    }
    let test = 4533582959013069253 / 6;
    console.log(test);
    console.log(answer);
    return answer;
}

// isDivisibleBy6("1*0"); // ["120","150","180"]
// isDivisibleBy6("*"); //["0","6"]
// isDivisibleBy6("*1"); // []
// isDivisibleBy6("81234567890*"); // ["812345678904"]
// isDivisibleBy6('318837704289243*5');
// isDivisibleBy6('9071*19656733560357'); // []
isDivisibleBy6('1234567890123456789012345678*0');
// ['123456789012345678901234567800', '123456789012345678901234567830', '123456789012345678901234567860', '123456789012345678901234567890']
// isDivisibleBy6('813634493573810*6615'); // []
// isDivisibleBy6('7933166*82368756');

// I'm not sure what math piece I'm missing here, but I feel like it is something about how I can look at a smaller
// piece of these enormous numbers to determine if any of them would be divisible by 6
