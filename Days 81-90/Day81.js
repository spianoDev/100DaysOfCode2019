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
// function twoSum(numbers, target) {
//     // variable for the values that create the target
//     let answer = [];
//     // loop through the array
//     for (let value of numbers) {
//         // compare the value with the difference from the target
//         if (target - value === numbers[0]){
//             answer.push(value, numbers[0]);
//         }
//     }
//     console.log(answer);
//     if (answer.length === 0){
//         answer.push(numbers[1]);
//         answer.push(numbers[2]);
//     }
//     // variable for the index where the answer can be found
//     let index = [];
//     // loop through the numbers again and return the index number for the found values
//     for (let i in numbers){
//         if (answer[0] === numbers[i]){
//             index.push(Number(i)) ;
//         } else if (answer[1] === numbers[i] && numbers[i] !== index[0]){
//             index.push(Number(i));
//         }
//
//     }
//     // return the matching index values
//     console.log(index);
//     return index;
//
// the above solution works only for the practice tests, so i'm trying a new approach

function twoSum(numbers, target) {
    // variable for the values that create the target
    let answer = [];
    // sort the array so comparing values to target is easier
    // but I want to retain the original values of the array
    let numberSort = numbers.slice().sort(function(a, b){return a - b});
    console.log(numberSort);
    // create two pointers to aid in comparison
    let pointer1 = 0;
    let pointer2 = numberSort.length -1;
    // cycle through the sorted array until pointers reach the end of the array
    while (pointer2 > pointer1) {
        // compare the value with the difference from the target
        if (numberSort[pointer1] + numberSort[pointer2] === target) {
            answer.push(numberSort[pointer1]);
            answer.push(numberSort[pointer2]);
            break;
        } else if (numberSort[pointer1] + numberSort[pointer2] < target) {
            pointer1 += 1;
        } else if (numberSort[pointer1] + numberSort[pointer2] > target) {
            pointer2 -= 1;
        }
    }
    console.log(answer);
    // need to make sure the answer index values are presented in order
    if (numbers.indexOf(answer[0] > numbers.indexOf(answer[1]))){
        console.log('switch them');
        let temp = answer[1];
        answer.pop();
        answer.unshift(temp);
        console.log(answer);
    }
    // variable for the index where the answer can be found
    let index = [];
    // loop through the numbers again and return the index number for the found values
    for (let i = 0; i < numbers.length; i++){
        if (index.length <= 1 && answer[0] === numbers[i]){
            console.log('answer 0 is ' + i);
            index.push(i);
        } if (i !== index[0] && answer[1] === numbers[i]){
            console.log('answer 1 is ' + i);
            index.push(i);
        }
    }
    // return the matching index values
    console.log(index);
    index = [...new Set(index)];
    console.log(index);
    console.log(numbers.indexOf(answer[0]));
    // if the duplicates removed still results in 3 index values, remove the first value
    if (index.length > 2) {
        if (index[0] !== numbers.indexOf(answer[0]) || index[1] !== numbers.indexOf(answer[0])) {
            index.shift();
        }  else if (index[1] !== numbers.indexOf(answer[1]) || index[2] !== numbers.indexOf(answer[1])) {
            index.pop();
        }
    }
    console.log('final answer ' + index);
    return index;
}

// twoSum([1,2,3], 4);
// twoSum([1234,5678,9012], 14690);
// twoSum([2,2,3], 4);
// twoSum([672, 972, 985, 593, 312, 26, 925, 534, 694, 742], target = 1667);
// twoSum([0, 263, 885, 151, 458, 792, 107, 616, 418, 785], target = 151);
// twoSum([717, 42, 7, 898, 280, 616, 440, 109, 988, 705], target = 896);
// twoSum(numbers = [413, 322, 430, 166, 433, 725, 592, 166, 861, 155], target = 1027);
// twoSum(numbers = [753, 271, 576, 783, 700, 898, 818, 942, 988, 38], target = 980);
// twoSum(numbers = [229, 643, 456, 156, 380, 156, 879, 763, 811, 49], target = 1035);
// twoSum(numbers = [568, 292, 222, 681, 681, 55, 514, 4, 831, 144], target = 1195);
twoSum(numbers = [547, 88, 682, 295, 472, 106, 191, 263, 617, 295], target = 977);

// only final example is not working... passing 504 examples
