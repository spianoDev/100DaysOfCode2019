// 6kyu on CodeWars: https://www.codewars.com/kata/5274d9d3ebc3030802000165/train/javascript

// Bob and Charles are meeting for their weekly jogging tour. They both start at the same spot called "Start" and they each run a different lap, which may (or may not) vary in length. Since they know each other for a long time already, they both run at the exact same speed.
//
//     Illustration
// Example where Charles (dashed line) runs a shorter lap than Bob:
//
//     Example laps
//
// Task
// Your job is to complete the function nbrOfLaps(x, y) that, given the length of the laps for Bob and Charles, finds the number of laps that each jogger has to complete before they meet each other again, at the same time, at the start.
//
//     The function takes two arguments:
//
//     The length of Bob's lap (larger than 0)
// The length of Charles' lap (larger than 0)
//
// The function should return an array (Tuple<int, int> in C#) containing exactly two numbers:
//
//     The first number is the number of laps that Bob has to run
// The second number is the number of laps that Charles has to run
//
// Examples:
//
//     nbrOfLaps(5, 3); // returns [3, 5]
// nbrOfLaps(4, 6); // returns [3, 2]

// need a function that finds prime numbers
function isPrime(num) {
    for (let i = 2; i < num; i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}
// need to add primes to a list of prime numbers
let primes = [];
for (let i = 2; i < 1000; i++){
    if (isPrime(i)) {
        primes.push(i);
    }
}
// console.log(primes);

let nbrOfLaps = function (x, y) {
    console.log('original x, y :' + x, y);
    let laps = [];
    // need to find a lowest common denominator for both laps by prime numbers
// loop through the primes array to determine if x and y are divisible by a prime
    for (let i = 0; i < primes.length; i++) {
        // console.log(primes[i]);
        if (x % primes[i] === 0 && y % primes[i] === 0) {
            x /= primes[i];
            y /= primes[i];
        }
    }
    // need to reduce by 2, 3, and 5 until lowest common denominator is reached
    while (x % 2 === 0 && y % 2 === 0) {
        x /= 2;
        y /= 2;
    } while (x % 3 === 0 && y % 3 === 0) {
        x /= 3;
        y /= 3;
    } while (x % 5 === 0 && y % 5 === 0) {
        x /= 5;
        y /= 5;
    }
// as long as the x and y values are not equal, Bob would run the number of Charles laps and vice versa
    if (x !== y) {
        laps.push(y);
        laps.push(x);
    } else {
        laps.push(1);
        laps.push(1);
    }
    console.log(x, y);
    console.log(laps);
    // return the values
    return laps;
};

// nbrOfLaps(5,3); // [3, 5]
// nbrOfLaps(4,6); // [3 ,2]
// nbrOfLaps(5, 5); // [1, 1]
// nbrOfLaps(5, 15); // [3, 1]
// nbrOfLaps(3984, 3200); // [200, 249]
// nbrOfLaps(7755, 6875); // [125, 141]
// nbrOfLaps(7450, 8925); // [357, 298]
// nbrOfLaps(3298, 3587); // [211, 194]
// nbrOfLaps(6777, 3263); // [13, 27]
// nbrOfLaps(2560, 8724);
nbrOfLaps(3834, 7965);
