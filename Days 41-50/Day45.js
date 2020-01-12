//6kyu on CodeWars: https://www.codewars.com/kata/514b92a657cdc65150000006/train/javascript

// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
// The sum of these multiples is 23.
//
// Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
//
// Note: If the number is a multiple of both 3 and 5, only count it once.

function solution(number){
    // I need to collect all the numbers between 1 and the given number in an array
    let allNumbers = [];
    // This will collect the sum of the numbers found inside the allNumbers array that fit the criteria
    let divNumbers = 0;
    // first I need to collect the numbers
    for (let i = number - 1; i > 0; i--) {
        allNumbers.push(i);
    }
    console.log(allNumbers);
    // Now I want to count the numbers that are divisible by both 3 and 5
    for (let number in allNumbers) {
        console.log(allNumbers[number]);
         if (allNumbers[number] % 5 === 0 && allNumbers[number] % 3 === 0) {
             divNumbers += allNumbers[number];
             console.log('both');
         } else if (allNumbers[number] % 5 === 0) {
             divNumbers += allNumbers[number];
             console.log('fives');
         } else if (allNumbers[number] % 3 === 0) {
             divNumbers += allNumbers[number];
             console.log('threes');
         }
    }
    console.log(divNumbers);
    return divNumbers;
}

solution(22);
