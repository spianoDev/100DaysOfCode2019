// 7kyu on CodeWars: https://www.codewars.com/kata/months-weeks-days-hours-and-minutes/train/javascript

// Given a number of minutes, translate it into a readible human timestamp.
//
// For example: 100 minutes equals "1 hour 40 minutes" And: 52874 minutes equals "1 month 1 week 1 day 17 hours 14 minutes"
//
// Given that each month has 28 days.
//
// The largest amount of minutes you'll have to test for is under a year so you'll have to translate it to Months, Weeks, Days, Hours and Minutes.

function displayValue(time) {
    // these are the values I need to be able to access:
    let months = Math.floor(time / 40320);
    // console.log(months + ' months');
    let weeks = Math.floor(time % 40320 / 10080);
    // console.log(weeks + ' weeks');
    let days = Math.floor(time % 10080 / 1440);
    // console.log(days + ' days');
    let hours = Math.floor(time % 1440 / 60);
    // console.log(hours + ' hours');
    let minutes = Math.floor(time % 60 % 60);
    // console.log(minutes + ' minutes');

    // this works, but it also returns plural for singular values and zero values which we don't want.
    // if (time) {
    //     return months + ' months ' + weeks + ' weeks ' + days + ' days ' + hours + ' hours ' + minutes + ' minutes';
    // }
    // so instead I will return the answer as an array of only relevant values each with their own if/else statements
    // starting with months and down to minutes.
    let answer = [];
    if (months === 1) {
        answer.push(months + ' month');
    } else if (months > 1) {
        answer.push(months + ' months');
    }
    if (weeks === 1) {
        answer.push(weeks + ' week');
    } else if (weeks > 1) {
        answer.push(weeks + ' weeks');
    }
    if (days === 1) {
        answer.push(days + ' day');
    } else if (days > 1) {
        answer.push(days + ' days');
    }
    if (hours === 1) {
        answer.push(hours + ' hour');
    } else if (hours > 1) {
        answer.push(hours + ' hours');
    }
    if (minutes === 1) {
        answer.push(minutes + ' minute');
    } else if (minutes > 1) {
        answer.push(minutes + ' minutes');
    }
    // finally joining the answer together:
    console.log(answer.join(" "));
    console.log(answer);
    return answer.join(" ");
}
displayValue(103801);

