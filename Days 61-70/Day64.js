// 5kyu on CodeWars: https://www.codewars.com/kata/52449b062fb80683ec000024/train/javascript

// The marketing team is spending way too much time typing in hashtags.
//     Let's help them with our own Hashtag Generator!
//
// Here's the deal:
//
// It must start with a hashtag (#).
//     All words must have their first letter capitalized.
//     If the final result is longer than 140 chars it must return false.
//     If the input or the result is an empty string it must return false.
//     Examples
// " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
// "    Hello     World   "                  =>  "#HelloWorld"
// ""                                        =>  false

function generateHashtag(s) {
    console.log(s);
    // first I need to split the string into the individual words
    let eachWord = s.split(' ');
    // next create an array that will hold the individual words
    let words = ['#'];
    for (let word of eachWord) {
        // the extra spaces will return 'undefined' so ignoring those...
        if (word[0] !== undefined) {
            // console.log(word[0]);
            // add the word with the first letter capital
            words.push(word.replace(word[0], word[0].toUpperCase()));
        }
    }
    // console.log(words);
    // if answer only has the # (it is empty) return 'false'
    if (words.length === 1) {
        return false;
    } else {
        // join the array together back into a single word
        let answer = words.join('');
        if (answer.length > 140) {
            return false;
        } else {
            console.log(answer);
            return answer;
        }
    }
}

generateHashtag("Do We have A Hashtag"); // #DoWeHaveAHashtag
// generateHashtag("code" + " ".repeat(140) + "wars"); // #CodeWars
