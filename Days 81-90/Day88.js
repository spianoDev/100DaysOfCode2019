// 5kyu on CodeWars: https://www.codewars.com/kata/51edd51599a189fe7f000015/train/javascript

// Complete the function that
//
// accepts two integer arrays of equal length
// compares the value each member in one array to the corresponding member in the other
// squares the absolute value difference between those two values
// and returns the average of those squared absolute value difference between each member pair.
//     Examples
//     [1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
//     [10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
//     [-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2

let solution = function(firstArray, secondArray) {
    // need variables to store results
    let differences = [];
    let answer = 0;
    // compare the values at each index and subtract one from the other adding the difference as an absolute value
    for (let i = 0; i < firstArray.length; i++) {
        differences.push(Math.abs(firstArray[i]-secondArray[i]) * Math.abs(firstArray[i]-secondArray[i]));
    }
    // take those squared values and return the average of them
    for (let j = 0; j < differences.length; j++) {
        answer += differences[j];
    }
    console.log(differences);
    answer /= differences.length;
    console.log(answer);
    return answer;
};

// solution([1,2,3],[4,5,6]); // 9
solution([10,20,10,2],[10,25,5,-2]); // 16.5
