//6kyu on CodeWars: https://www.codewars.com/kata/57b9d705f302997e61000157/train/javascript

// In this kata you're given a string which can include English lowercase letters, digits, and spaces.
// Your task is to write a function which will return a string of 'L' and 'R' chars which displays in which order should the hands be used to type it.
//
// Rules of touch typing
// The digits before (including) 5, letters of the first row before (including) t, letters of the second row before (including) g
// and letters of the third row before (including) b are typed with left hand, the other digits and numbers are typed with right hand.
// Space is typed with left hand if the non-space char you typed before was typed with right one, and vice versa.
// If it is the first char, it's typed with left hand.
// Every string you're given is a correct string which includes only digits, lowercase letters and spaces. Strings need not be validated.
//
// Examples
// "i love programming" -> "RLRRLLRRLRLLLRRRRL"
// " two spaces" -> "LLLLRLLRLLLL"

function touchType(str) {
    let handSequence = [];
    let leftChars = ['1','2','3','4','5','q','w','e','r','t','a','s','d','f','g','z','x','c','v','b'];
    // I will evaluate each character in the string to determine the hand used
    for (let char in str) {
        console.log(str[char]);
        if (str[char].includes(leftChars[0]) || str[char].includes(leftChars[1]) || str[char].includes(leftChars[2]) ||
            str[char].includes(leftChars[3]) || str[char].includes(leftChars[4]) || str[char].includes(leftChars[5]) ||
            str[char].includes(leftChars[6]) || str[char].includes(leftChars[7]) || str[char].includes(leftChars[8]) ||
            str[char].includes(leftChars[9]) || str[char].includes(leftChars[10]) || str[char].includes(leftChars[11]) ||
            str[char].includes(leftChars[12]) || str[char].includes(leftChars[13]) || str[char].includes(leftChars[14]) ||
            str[char].includes(leftChars[15]) || str[char].includes(leftChars[16]) || str[char].includes(leftChars[17]) ||
            str[char].includes(leftChars[18]) || str[char].includes(leftChars[19])) {
            handSequence.push('L');
        } else if (str[char] === ' ' && handSequence.length < 2) {
            handSequence.push('L');
        } else if (str[char] === ' ' && handSequence[handSequence.length-1] === 'R') {
            handSequence.push('L');
        } else {
            handSequence.push('R');
        }
    }
    console.log(handSequence);
    console.log(...leftChars);
    console.log(leftChars.length);
    return handSequence.join('');
}

touchType('  two spaces');
// I feel like this solution requires some explanation. I couldn't sleep so I woke in the middle of the night and
// decided to work on this algorithm. I couldn't get the spread operator to work and I was so close to the
// solution... I was also getting tired, so I just wrote out all the options for the lefChars and when it passed, I
// went back to bed. In looking at this (the next day) I'm a bit embarrassed that I actually submitted it this way.
