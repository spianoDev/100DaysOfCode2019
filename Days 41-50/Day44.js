//6kyu on CodeWars: https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/javascript

// The wave (known as the Mexican wave in the English-speaking world outside North America) is an example of metachronal
// rhythm achieved in a packed stadium when successive groups of spectators briefly stand, yell, and raise their arms.
// Immediately upon stretching to full height, the spectator returns to the usual seated position.
// The result is a wave of standing spectators that travels through the crowd, even though individual spectators never
// move away from their seats. In many large arenas the crowd is seated in a contiguous circuit all the way around the sport field,
// and so the wave is able to travel continuously around the arena; in discontiguous seating arrangements, the wave can
// instead reflect back and forth through the crowd. When the gap in seating is narrow, the wave can sometimes pass through it.
// Usually only one wave crest will be present at any given time in an arena, although simultaneous, counter-rotating waves have been produced.
// (Source Wikipedia)
//
// Task
// In this simple Kata your task is to create a function that turns a string into a Mexican Wave.
// You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.
//     Rules
// 1.  The input string will always be lower case but maybe empty.
// 2.  If the character in the string is whitespace then pass over it as if it was an empty seat.
//     Example
// wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

function wave(str){
    // before I do anything, I will tell the program to return an empty array if the str is empty
    if (str === '') {
        return [];
    }
    // I need a variable that eliminates all the spaces
    let letter = str.split('');

        console.log(letter);
    let upperCaseLetter = [];
    let wordArr = [];
    let newWordBeginning = [];
    let newWordEnd = [];
    for(let i = 0; i < letter.length; i++){
        // this is the letter I want to change
        upperCaseLetter.push(letter[i].toUpperCase());
        // now I want to replace this upperCaseLetter at the correct index within each new word
        // to do that I need to make two new pieces... before the change and after the change
        newWordBeginning.push(letter.slice(0, i+1).join(''));
        newWordEnd.push(letter.slice(i + 1, letter.length).join(''));
    }
    console.log('This is the beginning ' + newWordBeginning);
    console.log('This is the end ' + newWordEnd);
// now I need to put these together in order and return the new list
    wordArr.push(upperCaseLetter[0]+newWordEnd[0]);
    // I'm going to loop again to be sure I catch all the characters
    for (let j = 1; j < newWordEnd.length; j++) {
        wordArr.push(newWordBeginning[j-1] + upperCaseLetter[j] + newWordEnd[j]);
    }
    // in order to 'pass over the space' the last part is to get rid of the places where no capitals exist
    let filteredWordArr = wordArr.filter(function(value, index, arr) {
        if (value !== wordArr[index].toLowerCase()) {
            return value;
        }
    });
      console.log(filteredWordArr);
    return filteredWordArr;
}

wave('i can see');
