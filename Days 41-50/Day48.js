//5kyu on CodeWars: https://www.codewars.com/kata/5a3c7c151f7f70b19a00006f/train/javascript

// Write
//
// function findSubstring (s, words) {}
// that given a string, s, and a list of words, words, that are all of the same length.
// Find all starting indices of substring in s that is a concatenation of each word in words exactly once and without any intervening characters.
//
// For example:
//
// findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]) === [6, 9, 12]
// findSubstring("helloworld", ["world", "hello"]) === [0]
// findSubstring("helloworld", ["bar", "foo"]) === []

function findSubstring(s, words) {
    // I think I will start by comparing the string with the concatenation of the words.
    let completeWordChoices = [];
    let indexValues = [];
    let indexAnswers = [];
    // I need to add the case for the edge case of all the words entries being identical
    let allEqual = words => words.every( chars => chars === words[0] );

    if (allEqual(words)) {
        completeWordChoices.push(words.join(''));
        console.log(completeWordChoices);
        console.log(s.includes(completeWordChoices));
        let n = 0;
        while (s.includes(completeWordChoices, n)) {
            indexValues.push(s.indexOf(completeWordChoices, n));
            n++;
        }
        console.log(indexValues);
    } else {
    // I'm going to try making a variable that concatenates all the words in order and in reverse order
    // let longWord = words.join('');
    // let longReverse = words.reverse().join('');
    // So this had me on the right track, but I did a bit of research to discover a shuffle algorithm
    // based on the Fisher-Yates shuffle: https://javascript.info/task/shuffle
    //     console.log(s.length);
    for (let i = 0; i < s.length * 2; i++) {
            // I decided to go with the length of the words array 2X to statistically guarantee all possible
        // outcomes.
        shuffle(words);
        completeWordChoices.push(words.join(''));
        }
    }
    // now let's compare the choices to the string given.

    for (let newWord in completeWordChoices) {
        if (s.includes(completeWordChoices[newWord])) {
            // console.log('yes');
            // console.log(s.indexOf(completeWordChoices[newWord]));
            indexValues.push(s.indexOf(completeWordChoices[newWord]));
        }
    }
    // Now I need to sort these numbers and eliminate duplicates
    let sortedIndex = indexValues.sort(function(a, b){return a-b});
    indexAnswers = [...new Set(sortedIndex)];
    console.log(s);
    console.log(words);
    console.log(indexAnswers);
    return indexAnswers;
}
function shuffle(options) {
    for (let i = options.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        [options[i], options[j]] = [options[j], options[i]];
    }
}

findSubstring("aaaaaaaa", ["aa", "aa", "aa"]);
