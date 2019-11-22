// 7kyu on CodeWars: https://www.codewars.com/kata/sum-of-odd-cubed-numbers/train/javascript

// Find the sum of the odd numbers within an array, after cubing the initial integers.
// The function should return undefined/None/nil/NULL if any of the values aren't numbers.

function cubeOdd(arr) {
    let answer = 0;
    // I am going to start with a simple loop to iterate through the contents of the array.
    for (let i = 0; i < arr.length; i++) {
        // console.log(arr[i]);
        // console.log(typeof arr[i]);
        // first I want to eliminate any arrays that contain strings.
        if (typeof arr[i] === 'string') {
            return undefined;
        }
        // next I want to return only odd values.
        else {
            // I needed to adjust my original if statement since the % functions as a remainder and not modulus in
            // JavaScript.
            if (arr[i] % 2 === 1 || arr[i] % 2 === -1) {
                let cubedNumbers = Math.pow(arr[i], 3);
                console.log(arr[i]);
                //console.log(cubedNumbers);
                answer += cubedNumbers;
            }
        }
        // console.log(answer);
     }
return answer;
}
cubeOdd([-3,-2]);
console.log(cubeOdd([-3,-2]));
