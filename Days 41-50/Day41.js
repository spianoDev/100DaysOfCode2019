//  7kyu on CodeWars: https://www.codewars.com/kata/jaden-casing-strings/train/javascript

// Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013).
// Jaden is also known for some of his philosophy that he delivers via Twitter.
// When writing on Twitter, he is known for almost always capitalizing every word.
// For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.
//
// Your task is to convert strings to how they would be written by Jaden Smith.
// The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.
//
//     Example:
//
// Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
// Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't
let str = "How can mirrors be real if our eyes aren't real";

String.prototype.toJadenCase = function () {
    // I need a variable to store the answer
    let newString = [];
    // First I'm going to split up the sentence by the space separating the words so I can access each word separately
    let eachWord = this.split(' ');
    // Next I will loop through the words and change the first letter of each word
    for (let word in eachWord){
         // console.log(eachWord[word]);
        // console.log(eachWord[word][0].toUpperCase());
        newString.push(eachWord[word].replace(eachWord[word][0],eachWord[word][0].toUpperCase()));
        // console.log(newString);

    }
    // Finally I need to put the word back into a string
    let answer = newString.join(" ");
    console.log(answer);
    return answer;
};

console.log(str.toJadenCase());

