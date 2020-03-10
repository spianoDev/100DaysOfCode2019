// 6kyu on CodeWars: https://www.codewars.com/kata/573c84bf0addf9568d001299/train/javascript

// Write a code that receives an array of numbers or strings, goes one by one through it while taking one value out, leaving one value in, taking, leaving, and back again to the beginning until all values are out.
//     It's like a circle of people who decide that every second person will leave it, until the last person is there. So if the last element of the array is taken, the first element that's still there, will stay.
//     The code returns a new re-arranged array with the taken values by their order. The first value of the initial array is always taken.
//
//     Examples:
//
// var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
// // returns [1, 3, 5, 7, 9, 2, 6, 10, 8, 4]
//
// var arr = ['this', 'code', 'is', 'right', 'the']
// // returns ['this', 'is', 'the', 'right', 'code']

// function yesNo(arr){
//     console.log(arr);
//     // create two variables to hold the new order of the arrays
//     let evens = [];
//     let oddsLeft = [];
//     let oddsRight = [];
//     // loop through the original arr and add the even values to the first array
//     for (let i = 0; i < arr.length; i++) {
//         if (i % 2 === 0) {
//             evens.push(arr[i]);
//             // arr.splice(i, 1);
//         } else if (i % 4 === 1) {
//             // add the odd values to the second and third array
//             oddsLeft.push(arr[i]);
//         } else {
//             oddsRight.unshift(arr[i]);
//         }
//
//     }
//     console.log(evens, oddsLeft, oddsRight);
//     // put the odd side together
//     let odds;
//     if (oddsRight.length === 1 && oddsLeft.length === 1) {
//         odds = oddsRight.concat(oddsLeft);
//     } else {
//         odds = oddsLeft.concat(oddsRight);
//     }
//     console.log(odds);
//     // put the odd and even arrays together
//     let answer = evens.concat(odds);
//     console.log(answer);
//     return answer;
// }

// tried the above solution, but it didn't quite work...



// yesNo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]); // [1, 3, 5, 7, 9, 2, 6, 10, 8, 4]
// yesNo(['this', 'code', 'is', 'right', 'the']); // ['this', 'is', 'the', 'right', 'code']
yesNo([ 'L', 'W', 'P', 'V', 'K', '3' ]); // ['L', 'P', 'K', 'W', '3', 'V']
// yesNo([ '2', '5', 'p', 'e', 'f', 'x', 'P', '4', 'e' ]); // ['2', 'p', 'f', 'P', 'e', 'e', '4', 'x', '5']

