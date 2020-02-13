// 5kyu on CodeWars: https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/javascript

// Write an algorithm that takes an array and moves all of the zeros to the end,
// preserving the order of the other elements.
//
// moveZeros([false,1,0,1,2,0,1,3,"a"]) // returns[false,1,1,2,1,3,"a",0,0]

let moveZeros = function (arr) {
    // I need a variable to hold the zeros
    let zeros = [];
    // This variable will put everything else from original array in original order
    let newArr = [];
    // next I will loop through the contents of the existing array and if the value is zero, remove it
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 0) {
            zeros.push(arr[i]);

        } else {
            newArr.push(arr[i]);
        }
    }
    console.log(newArr);
    console.log(zeros);
    // concat the two arrays together
    let answer = newArr.concat(zeros);
    console.log(answer);
    return answer;
};

moveZeros([false,1,0,1,2,0,1,3,"a"]);
