//  6kyu on CodeWars: https://www.codewars.com/kata/5d5a7525207a674b71aa25b5/train/javascript

// Given a triangle of consecutive odd numbers:
// //
// //     1
// // 3     5
// // 7     9    11
// // 13    15    17    19
// // 21    23    25    27    29
// // ...
// // find the triangle's row knowing its index (the rows are 1-indexed), e.g.:
// //
// // odd_row(1)  ==  [1]
// // odd_row(2)  ==  [3, 5]
// // odd_row(3)  ==  [7, 9, 11]
// // Note: your code should be optimized to handle big inputs.

function oddRow(n) {
    // first I need a loop to eliminate all the numbers in previous rows
    let sum = 0;
    for (let i = 1; i <= n; i++) {
        sum += i;
    }
    // then I need to multiply that sum by 2
    sum *= 2;
    console.log(sum);
    // The n row will start on the next odd number after this sum and will go for the length of the row
    let rowLength = sum - (n * 2) + 1;
    console.log(rowLength);
    let answer = [];
    for (let row = rowLength; row < sum; row += 2) {
        // console.log(row); This gives the answer, so now I need to add them to an array to return
        answer.push(row);
    }
    console.log(answer);
    return answer;
}

// oddRow(2); // [3,5]
oddRow(13); // [157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181]
