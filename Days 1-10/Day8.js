// 7kyu on CodeWars: https://www.codewars.com/kata/return-the-closest-number-multiple-of-10/train/javascript

// Given a number return the closest number to it that is divisible by 10.
//
// Example input:
//
// 22
// 25
// 37
// Expected output:
//
// 20
// 30
// 40

const closestMultiple10 = num => {
    // this one should be a simple Math.floor conversion.
    // I need to both round the number to the nearest 10 so that means first dividing and then multiplying ten after
    // it is rounded.
    let roundedNumber = Math.round(num/10) * 10;
    console.log(roundedNumber);
    return roundedNumber;
};

closestMultiple10(56);
