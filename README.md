# 100DaysOfCode2019

## A place where I show algorithmic problems and solutions in JavaScript and Python.

Please note the code will be organized by days and will include many comments to demonstrate my thinking as I work through the problem. This is much like a whiteboarding challenge and all answers are verified on [codewars](https://www.codewars.com/dashboard). Please visit the link to see more challenges.

Initially I wanted to only complete challenges that were algorithms but as December hit, I changed direction to 'themed' Kata specific to the upcoming holiday. Here is an example of a Christmas themed 6kyu javascript problem:

```javascript

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
```
