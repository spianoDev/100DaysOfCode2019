//  6kyu on CodeWars: https://www.codewars.com/kata/5e18743cd3346f003228b604/train/javascript

// Ask a mathematician: "What proportion of natural numbers contain at least one digit 9 somewhere in their decimal representation?"
//
// You might get the answer "Almost all of them", or "100%".
//
//     Clearly though, not all whole numbers contain a 9.
//
// In this kata we ask the question: "How many Integers in the range [0..n] contain at least one 9 in their decimal representation?"
//
// In other words, write the function:
//
//     nines :: BigInt => BigInt
// Where, for example:
//
// nines(1n)  = 0n
// nines(10n) = 1n     // 9
// nines(90n) = 10n    // 9, 19, 29, 39, 49, 59, 69, 79, 89, 90
// When designing your solution keep in mind that your function will be tested against some large numbers (up to 10^38)

function nines(n) {
    // I haven't worked with BigInt before, so I did some experimentation with conversion to Number first
    // Convert 'n' into a regular number
    const num = Number(n);
    // console.log(typeof num);
    // console.log(num);
    // console.log(BigInt(num));
    // a counter to keep track of the number of nines
    let count = 0;
    // loop through all the integers between 0 and 'n' to see any digits are '9'

    for (let i = 0; i <= num; i++) {
        // I need to convert the number into a string to check for the '9'
        let nines = i.toString().includes('9');
        if (nines) {
            count += 1;
        }
    }
    // return the total as a BigInt number
    // console.log(count);
    return BigInt(count);
}
// nines(1n); // 0n
// nines(10n); // 1n
// nines(90n); // 10n
// nines(100n); // 19n
// nines(1000n); // 271n

// The above solution works, but is not efficient since it requires every 'i' value to convert to a string



