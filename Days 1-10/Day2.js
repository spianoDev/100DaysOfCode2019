// 8kyu on CodeWars: https://www.codewars.com/kata/convert-a-string-to-a-number/train/javascript


//We need a function that can transform a string into a number. What ways of achieving this do you know?
//
// Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.
//
// Examples
// stringToNumber("1234") == 1234
// stringToNumber("605" ) == 605
// stringToNumber("1405") == 1405
// stringToNumber("-7"  ) == -7

// the original format wanted to use a variable declared function, so I will demo that version of the function.

 let stringToNumber = function(str){
    // there is a built in function in JS that will take a string and convert it to an integer:
    return parseInt(str);
};

console.log(stringToNumber("1234"));
// No refactoring required on this one.
