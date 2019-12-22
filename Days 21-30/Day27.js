// 7kyu on CodeWars: https://www.codewars.com/kata/holiday-array-repair/train/javascript
//
// The Problem
// A colleague has been working on a program that returns the number of days of holiday that people in your coding company can take in the remainder of the year.
// The colleague’s program outputs the number of holidays each employee has left as an integer within an array.
// However, the program is not working properly. Alongside the element that specifies the number of holidays are several other useless elements.
// These other elements are of a variety of data types and none are integers.
// Your colleague boasts that he has more days of holiday left than you.
//
// Your Task
// Array1 contains one integer that specifies the number of days of holiday that your colleague has left.
// Array2 contains one integer with the number of days of holiday that you have left.
// Each of the two arrays will never contain more than a single integer.
//
// If your colleague is telling the truth, the function should return the string "Right".
// If your colleague is wrong, the function should return the string "Wrong".
// If you both have the same number of days of holiday, the function should return the string 'Same'.
// If your colleague's program is beyond repair and does not produce an integer in both arrays, the function should return a string 'Not possible'.

function holidayCount (peerDays, myDays){
    let peerHolidays;
    let myHolidays;
// First I need to access the value that is the integer and throw out the rest of the useless parts of the array.
    // Since the sort function will order the array with numbers first, I can just pull the first return after sorting.
console.log(peerDays.sort());
    peerHolidays = peerDays.sort()[0];
    myHolidays = myDays.sort()[0];
    // Now I will add the conditionals
    if (peerHolidays > myHolidays) {
        return 'Right';
    } else if (myHolidays > peerHolidays) {
        return 'Wrong';
    } else if (myHolidays === peerHolidays) {
        return 'Same';
    } else {
        return 'Not possible'
    }

}

console.log(holidayCount(["g", 3, "a"], ["j", 2, "r"]));
