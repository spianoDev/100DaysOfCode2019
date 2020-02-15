// 5kyu on CodeWars: https://www.codewars.com/kata/52dd72494367608ac1000416/train/javascript

// Preface
// A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
//
//     A more detailed description of prime numbers can be found at: http://en.wikipedia.org/wiki/Prime_number
//
//     The Problem
// You will need to create logic for the following two functions: isPrime(number) and getPrimes(start, finish)
//
// isPrime(number)
// Should return boolean true if prime, otherwise false
//
// getPrimes(start, finish)
// Should return a unique, sorted array of all primes in the range [start, finish] (i.e. both numbers inclusive). Note that this range can go both ways - e.g. getPrimes(10, 1) should return all primes from 1 to 10 both inclusive.
//
//     Sample Input:
//     isPrime(number):
//
// isPrime(0); // === false
// isPrime(1); // === false
// isPrime(2); // === true
// isPrime(3); // === true
// isPrime(4); // === false
// isPrime(5); // === true
// getPrimes(start, finish):
//
// getPrimes(0, 0); // === []
// getPrimes(0, 30); // === [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
// getPrimes(30, 0); // === [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

// these two functions will use elements from an earlier #100DaysOfCode challenge
// I love when I can reuse code!
function isPrime(number) {
    // anything less than 2 is false
    if (number < 2) {
        console.log(false);
        return false;
    } else if (number % 2 === 0) {
        // all even numbers
    }
    for (let p = 2; p < number; p++){
        // any number that doesn't have a remainder will not be prime
        if (number % p === 0) {
            console.log(false);
            return false;
        }
    }
    console.log(true);
    return true;
}
isPrime(11);

function getPrimes(start, finish) {
    // first I need a conditional to determine what the number limit is
    let limit;
    if (start > finish) {
        limit = start;
    } else {
        limit = finish;
    }
    // this formula comes from Day66.js
    let primes = [];
    let allNums = [];
    // need a loop to gather all the numbers that only divide by themselves and 1
    for (let i = 2; i <= limit; i++) {
        if (!allNums [i]) {
            primes.push(i);
            // use the << operator to round up.
            for (let j = i << 1; j <= limit; j += i) {
                allNums[j] = true;
            }
        }
    }
    console.log(primes);
    // Now I need to eliminate the values that are less than the start/finish in the primes array
    let answer = [];
    for (let j = 0; j < primes.length; j++) {
        if (start < finish && primes[j] < start) {
            console.log('start smaller ' + j);
        } else if (finish < start && primes[j] < finish) {
            console.log('finish smaller ' + j);
        } else {
            answer.push(primes[j]);
        }
    }
    console.log(answer);
    return answer;
}
getPrimes(30, 8);
