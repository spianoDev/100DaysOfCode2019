//  6kyu on CodeWars: https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/javascript

// Write a function that takes an array of numbers (integers for the tests) and a target number.
//     It should find two different items in the array that, when added together, give the target value.
//     The indices of these items should then be returned in a tuple like so: (index1, index2).
//
//     For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.
//
//     The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers;
//     target will always be the sum of two different items from that array).
//
// Based on: http://oj.leetcode.com/problems/two-sum/
//
//     twoSum [1, 2, 3] 4 === (0, 2)

function twoSum(numbers, target) {
    // variable for the values that create the target
    let answer = [];
    // loop through the array
    for (let value of numbers) {
        // compare the value with the difference from the target
        if (target - value === numbers[0]){
            answer.push(value, numbers[0]);
        }
    }
    console.log(answer);
    if (answer.length === 0){
        answer.push(numbers[1]);
        answer.push(numbers[2]);
    }
    // variable for the index where the answer can be found
    let index = [];
    // loop through the numbers again and return the index number for the found values
    for (let i in numbers){
        if (answer[0] === numbers[i]){
            index.push(Number(i)) ;
        } else if (answer[1] === numbers[i] && numbers[i] !== index[0]){
            index.push(Number(i));
        }

    }
    // return the matching index values
    console.log(index);
    return index;
}

// twoSum([1,2,3], 4);
twoSum([1234,5678,9012], 14690);
