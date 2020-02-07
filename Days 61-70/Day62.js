//  6kyu on CodeWars: https://www.codewars.com/kata/55b080eabb080cd6f8000035/train/javascript

// Write a function that will take in a string and return all the unpaired characters (show up an odd number of times in the string)
// in the order they were encountered as an array. In case of multiple options to choose from, take the last
// occurrence as the unpaired character.
//
//     Notes
// A wide range of characters is used, and some of them may not render properly in your browser.
//     Your solution should be linear in terms of string length to pass the last test.
//     Examples
// oddOneOut('Hello World')   ===  ["H", "e", " ", "W", "r", "l", "d"]
// oddOneOut('Codewars')      ===  ["C", "o", "d", "e", "w", "a", "r", "s"]
// oddOneOut('woowee')        ===  []
// oddOneOut('wwoooowweeee')  ===  []
// oddOneOut('racecar')       ===  ["e"]
// oddOneOut('Mamma')         ===  ["M"]
// oddOneOut('Mama')          ===  ["M", "m"]

// function oddOneOut(string) {
//     // first set up the frequency object to count the number of times each character appears
//     let frequency = {};
//     for (let char of string) {
//         frequency[char] = (frequency[char] || 0) + 1;
//     }
//     // two arrays of all the keys and values in the frequency object
//     console.log(frequency);
//     let allChars = Object.keys(frequency);
//     console.log(allChars);
//     let howManyChars = Object.values(frequency);
//     console.log(howManyChars);
//     // need a loop to add the < 1 odd values
//     let placement = [];
//     let character = [];
//     for (let i = 0; i < allChars.length; i++) {
//         if (howManyChars[i] % 2 === 1 && howManyChars[i] !== 1) {
//             let index = string.lastIndexOf(allChars[i]);
//             placement.push(-(string.length - index));
//             character.push(allChars[i]);
//             console.log(placement);
//         }
//     }
//             // another loop through the frequency arrays (they are the same length so this makes it easier) to add to the answer
//             let answer = [];
//             for (let j = 0; j < allChars.length; j++) {
//                 if (howManyChars[j] === 1){
//                     answer.push(allChars[j]);
//                 }
//                 }
//
//             // need a separate loop to manage the deletion of the characters
//             for (let c = allChars.length-1; c === 0; c--) {
//                 if (howManyChars[c] === 1) {
//                     console.log(allChars[c]);
//                     allChars.splice(c, 1);
//                 } if (howManyChars[c] % 2 === 0) {
//                     console.log(allChars[c]);
//                     allChars.splice(c, 1);
//                 }
//             }
//     // console.log('this is what is left: ' + allChars);
//             console.log(answer);
//
//             // now need to add in the keys with > 1 values into correct place
//     for (let k = 0; k < placement.length; k++) {
//         if (placement[k] < -1) {
//             // insert the value
//             placement[k] += 1;
//             answer.splice(placement[k], 0, character[k]);
//         } else if (placement[k] === -1){
//             // add the value to the end
//         }
//     }
//             console.log(answer);
//             return answer;
//     }
// oddOneOut('Hello World'); // ["H", "e", " ", "W", "r", "l", "d"]
// oddOneOut('Mama'); // ["M", "m"]
function oddOneOut(string) {
    console.log(string);
    // first set up the frequency object to count the number of times each character appears
    let frequency = {};
    for (let char of string) {
        frequency[char] = (frequency[char] || 0) + 1;
    }
    // two arrays of all the keys and values in the frequency object
    console.log(frequency);
    let allChars = Object.keys(frequency);
    console.log(allChars);
    let howManyChars = Object.values(frequency);
    console.log(howManyChars);
    // need a loop to add the < 1 odd values
    let pointer = 0;
    let answer = [];
    // another loop through the frequency arrays (they are the same length so this makes it easier) to add to the answer
    for (let i = 0; i < string.length; i++) {
        if (howManyChars[pointer] === 1 && allChars[pointer] === string[i]) {
            answer.push(string[i]);
            pointer += 1;
        }
        if (howManyChars[pointer] % 2 === 1 && howManyChars[pointer] > 1 && allChars[pointer] === string[i]) {
            i += 1;
            pointer += 1;
        }
        if (howManyChars[pointer] % 2 === 1 && allChars[pointer] === string[i]) {
            pointer += 1;
            i += 1;
        }
        if (howManyChars[pointer] % 2 === 1 && howManyChars[i] !== 1 && allChars[pointer] !== string[i]) {
            let index = string.lastIndexOf(allChars[i]);
            console.log(index);
        }
    }

    console.log(answer);
    // return answer;
}
oddOneOut('Hello World'); // ["H", "e", " ", "W", "r", "l", "d"]
// oddOneOut('¼ x 4 = 1'); // ["¼", "x", "4", "=", "1"]

// this solution doesn't seem to be bringing me closer either.
