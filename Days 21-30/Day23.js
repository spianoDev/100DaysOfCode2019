//  6kyu on CodeWars: https://www.codewars.com/kata/christmas-day/train/javascript

// Sometimes it's useful to know on which day of the week Christmas, the holly holiday, will occur.
// Write a function which takes the date of Christmas, and outputs the day of the week it falls on.
// Just don't limit yourself to this year.
//
// Example:
//
// findOutChristmasWeekday('2013 12 25') // returns 'Wednesday'
// Only valid Christmas dates will be passed to the function.
//
// Date parameter could be a string or a Date object. If it's a string here are possible date parameter formats:
//
// '2013 12 25'
// '12 25 2013'
// '25 December 2013'

// Since I had used the DateTime methods in python, I suspected there was something equivalent in Javascript.
// This is the resource I found: https://www.digitalocean.com/community/tutorials/understanding-date-and-time-in-javascript

function findOutChristmasWeekday(date) {
    // first I will set a new variable to the date as a date object
    const christmas = new Date(date);
    console.log(christmas.getDay());
    // the above console gives me exactly what I was expecting. So now I need to convert it to the return value of
    // the day of the week
    if (christmas.getDay() === 0) {
        return 'Sunday';
    } else if (christmas.getDay() === 1) {
        return 'Monday';
    } else if (christmas.getDay() === 2) {
        return 'Tuesday';
    } else if (christmas.getDay() === 3) {
        return 'Wednesday';
    } else if (christmas.getDay() === 4) {
        return 'Thursday';
    } else if (christmas.getDay() === 5) {
        return 'Friday';
    } else {
        return 'Saturday';
    }
}
console.log(findOutChristmasWeekday('2013 12 25'));
