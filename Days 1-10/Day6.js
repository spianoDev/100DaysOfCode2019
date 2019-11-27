// 7kyu on CodeWars: https://www.codewars.com/kata/beginner-series-number-3-sum-of-numbers/train/javascript

//Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.
//
// Note: a and b are not ordered!
//
// Examples
// GetSum(1, 0) == 1   // 1 + 0 = 1
// GetSum(1, 2) == 3   // 1 + 2 = 3
// GetSum(0, 1) == 1   // 0 + 1 = 1
// GetSum(1, 1) == 1   // 1 Since both are same
// GetSum(-1, 0) == -1 // -1 + 0 = -1
// GetSum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

function getSum( a,b ) {
    // I need a variable to store the values
    let sum = 0;
    // first conditional will be if the numbers are the same.
    if (a === b) {
        return a;
    } else if (a > b) {
        // I want to add each number between the two numbers so I will use a for loop to do that.
        for (let i = b; i <= a; i++){
            sum += i;
        }
        // since the numbers are not ordered, the reverse is also true
    } else {
        for (let j = a; j <= b; j++) {
            sum += j;
        }
    }
    console.log(sum);
    return sum;
}
getSum(-1, 2);
