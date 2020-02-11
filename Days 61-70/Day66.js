// 6kyu on CodeWars: https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124/train/javascript

// Definition (Primorial Of a Number)
// Is similar to factorial of a number, In primorial, not all the natural numbers get multiplied,
// only prime numbers are multiplied to calculate the primorial of a number. It's denoted with P#.
//
// Task
// Given a number N , calculate its primorial. !alt !alt
//
// Notes
// Only positive numbers will be passed (N > 0) .
//     Input >> Output Examples:
//     1- numPrimorial (3) ==> return (30)
// Explanation:
//     Since the passed number is (3) ,Then the primorial should obtained by multiplying 2 * 3 * 5 = 30 .
//
//     Mathematically written as , P3# = 30 .
// 2- numPrimorial (5) ==> return (2310)

function numPrimorial(n){
    // need an edge case of n = 1
    if (n === 1) {
        console.log(2);
        return 2;
    }
    //find 'n' prime numbers
    let limit = n * n;
    let primes = [];
    let allNums = [];
    // need a loop to gather all the numbers that only divide by themselves and 1
    for (let i = 2; i <= limit; i++) {
        // console.log(allNums[i]);
            if (!allNums [i]) {
                primes.push(i);
                // use the << operator to round up.
                for (let j = i << 1; j <= limit; j += i)
                {
                    allNums[j] = true;
                }
            // console.log(allNums);
        }
    }
    console.log(primes);
    // multiply the 'n' primes together
    let answer = 1;
    for (let p = 0; p < n; p++) {
        answer *= primes[p];
    }
    console.log(answer);
    return answer;
}

numPrimorial(1); // 2
// numPrimorial(5); // 2310
