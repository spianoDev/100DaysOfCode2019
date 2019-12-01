// 7kyu on CodeWars: https://www.codewars.com/kata/sum-of-a-sequence/train/javascript

//Your task is to make function, which returns the sum of a sequence of integers.
//
// The sequence is defined by 3 non-negative values: begin, end, step.
//
// If begin value is greater than the end, function should returns 0
//
// Examples
//
// sequenceSum(2,2,2) === 2
// sequenceSum(2,6,2) === 12 // 2 + 4 + 6
// sequenceSum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
// sequenceSum(1,5,3) === 5 // 1 + 4

const sequenceSum = (begin, end, step) => {
    // I will need a sum value to put the answer into
    let sum = 0;
    // I'm going to begin with the conditional that would mean no computation
    if (begin > end) {
        return 0;
    } else {
        // Now I will need a loop to add values between the begin and end numbers.
        for (let i = begin; i <= end; i += step) {
            console.log(i);
            sum += i;
        }
    }
    console.log(sum);
    return sum;
};
sequenceSum(1,5,3);
